#!/bin/bash
set -e

# PUID/PGID Configuration (defaults to root if not set)
PUID=${PUID:-0}
PGID=${PGID:-0}

# Data directory configuration
DATA_DIR="/data"
CONFIG_DIR="$DATA_DIR/config"
OPENCODE_DIR="$DATA_DIR/.opencode"

# Export environment variables for the running application
export DATA_DIR
export CONFIG_DIR
export OPENCODE_DIR

# Create the complete directory structure
create_directories() {
    echo "Creating OpenCode data directories..."
    
    # Main directories
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$OPENCODE_DIR"
    
    # .opencode subdirectories for custom agents, commands, modes, plugins, skills, tools, themes
    mkdir -p "$OPENCODE_DIR/agents"
    mkdir -p "$OPENCODE_DIR/commands"
    mkdir -p "$OPENCODE_DIR/modes"
    mkdir -p "$OPENCODE_DIR/plugins"
    mkdir -p "$OPENCODE_DIR/skills"
    mkdir -p "$OPENCODE_DIR/tools"
    mkdir -p "$OPENCODE_DIR/themes"
    
    # Symlink for config directory to enable single-volume persistence
    mkdir -p /root/.config
    if [ ! -L /root/.config/opencode ]; then
        ln -sf "$CONFIG_DIR" /root/.config/opencode
    fi
    
    # Symlink for opencode data directory (auth.json, logs, etc.)
    mkdir -p /home/node/.local/share
    if [ ! -L /home/node/.local/share/opencode ]; then
        ln -sf "$OPENCODE_DIR" /home/node/.local/share/opencode
    fi
    
    echo "Directory structure created successfully."
}

# Set ownership of data directories
set_ownership() {
    if [ "$PUID" -ne 0 ] || [ "$PGID" -ne 0 ]; then
        echo "Setting ownership to PUID=$PUID, PGID=$PGID..."
        chown -R "$PUID:$PGID" "$DATA_DIR"
        chown -R "$PUID:$PGID" /root/.config
        chown -R "$PUID:$PGID" /home/node/.local
    fi
}

# Create user if PUID/PGID are specified
create_user() {
    if [ "$PUID" -ne 0 ] || [ "$PGID" -ne 0 ]; then
        # Check if group exists, create if not
        if ! getent group "$PGID" > /dev/null 2>&1; then
            groupadd -g "$PGID" opencode
        fi
        
        # Check if user exists, create if not
        if ! id -u "$PUID" > /dev/null 2>&1; then
            useradd -u "$PUID" -g "$PGID" -d /root -s /bin/bash opencode
        fi
    fi
}

# Build the opencode serve command
build_command() {
    # Start with the command "serve"
    local cmd="serve"
    
    # 1. Handle Port
    if [ -n "$PORT" ]; then
        cmd="$cmd --port $PORT"
    fi
    
    # 2. Handle Hostname (default to 0.0.0.0 in Docker)
    if [ -n "$HOSTNAME_OVERRIDE" ]; then
        cmd="$cmd --hostname $HOSTNAME_OVERRIDE"
    else
        cmd="$cmd --hostname 0.0.0.0"
    fi
    
    # 3. Handle mDNS
    if [ "$MDNS" = "true" ]; then
        cmd="$cmd --mdns"
    fi
    
    # 4. Handle mDNS Domain
    if [ -n "$MDNS_DOMAIN" ]; then
        cmd="$cmd --mdns-domain $MDNS_DOMAIN"
    fi
    
    # 5. Handle CORS (comma-separated list)
    if [ -n "$CORS" ]; then
        IFS=',' read -ra ORIGINS <<< "$CORS"
        for origin in "${ORIGINS[@]}"; do
            cmd="$cmd --cors $(echo $origin | xargs)"
        done
    fi
    
    echo "$cmd"
}

# Main execution
main() {
    # Create directory structure
    create_directories
    
    # Create user if needed
    create_user
    
    # Set ownership
    set_ownership
    
    # Build command
    COMMAND=$(build_command)
    
    echo "Starting opencode server..."
    
    # Ensure OPENCODE_CONFIG is exported if set
    if [ -n "$OPENCODE_CONFIG" ]; then
        export OPENCODE_CONFIG
    fi
    
    # Execute as the appropriate user
    if [ "$PUID" -ne 0 ] || [ "$PGID" -ne 0 ]; then
        # Drop privileges using gosu
        exec gosu "$PUID:$PGID" opencode $COMMAND "$@"
    else
        # Run as root (not recommended)
        exec opencode $COMMAND "$@"
    fi
}

# Run main function
main "$@"