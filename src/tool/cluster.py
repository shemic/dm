#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:docker.py
    author:rabin
"""
from core import *
from docker import *

class Cluster(Docker):
	@classmethod
	def init(self):
		action = ('uprun', 'restart','run', 'rm', 'rmb', 'show', 'reset', 'logs', 'update', 'inspect', 'test')
		super(Cluster, self).init(action, Cluster_Action)

	@classmethod
	def network(self):
		Swarm.network(self, self.conf['base'])

	@classmethod
	def handle(self, method, config, item, action='run', slave=False):
		if slave == False:
			self.rely(config, action)
		if 'cluster' in config:
			config['num'] = config['cluster']
		if 'num' not in config:
			config['num'] = 1
		num = int(config['num'])
		name = self.name(item, 1)
		if 'image' not in config:
			config['image'] = item
		if self.store == 'private' and config['image'] in self.core['images']:
			config['image'] = self.core['images'][config['image']]
		method(config=config, name=name, item=item, index=num, action=action)
		if action in ('update', 'restart', 'rm', 'rmb', 'reset', 'run', 'uprun'):
			time.sleep(2)
			self.slave(method, config, item, action)
		if slave == False:
			self.next(config, action)

class Cluster_Action(Docker_Action):

	@staticmethod
	def leave():
		result = Swarm.leave()
		print result

	@staticmethod
	def drop():
		Swarm.drop()
		print 'drop cluster:yes'

	@staticmethod
	def name():
		arg = Args.name
		name = Swarm.name(arg)
		name = name.split("\n")
		print name[0]

	@staticmethod
	def names():
		arg = Args.name
		name = Swarm.name(arg)
		print name

	@staticmethod
	def node():
		Swarm.node()

	@staticmethod
	def num():
		name = Args.name
		num = Args.param
		print 'setting ' + name + ', please wait...'
		Swarm.scale(name, num)

	@staticmethod
	def restart(**param):
		print 'reloading ' + param['name'] + ', please wait...'
		name = Swarm.name(param['name'])
		name = name.split("\n")
		for i in name:
			if i:
				Core.shell('container.restart ' + name, True, bg=True)

	@staticmethod
	def show(**param):
		name = ''
		if param:
			name = param['name']
		Swarm.show(name)

	@staticmethod
	def logs(**param):
		Swarm.logs(param['name'])

	@staticmethod
	def update(**param):
		Swarm.run(param['name'])

	@staticmethod
	def inspect(**param):
		Swarm.inspect(param['name'])

	@staticmethod
	def stop(**param):
		print 'stop command is not exists'

	@staticmethod
	def save(**param):
		tar,backup = Cluster.tar(param['name'])
		Swarm.save(tar, param['name'], backup)

	@classmethod
	def load(self, **param):
		tar,backup = Cluster.tar(param['name'])
		Swarm.load(tar, param['name'])
		Cluster.storeHost = ''
		param['config']['image'] = backup
		param['action'] = 'run'
		self.run(**param)

	@classmethod
	def uprun(self, **param):
		Image.install(Cluster.storeHost, param['config']['image'])
		param['action'] = 'run'
		self.run(**param)

	@staticmethod
	def rm(**param):
		if param and 'name' in param:
			Swarm.delete(param['name'])
			Alias.delete(param['config'], param['name'])
		else:
			Container.delete()
			print 'rm cluster:yes'

	@staticmethod
	def rmb(**param):
		if param and 'name' in param:
			Swarm.delete(param['name'], bg=True)
			Alias.delete(param['config'], param['name'])
		else:
			Swarm.delete()
			print 'rm cluster:yes'

	@classmethod
	def reset(self, **param):
		self.rm(**param)
		self.up(**param)

	@classmethod
	def test(self, **param):
		param['test'] = True
		print self.run(**param)

	@classmethod
	def create(self, **param):
		self.run(**param)

	@classmethod
	def call(self, **param):
		self.run(**param)

	@classmethod
	def run(self, **param):
		command = ''
		state = Swarm.check(param['name'])
		if state == 0:
			Cluster.hook('start', param['config'], param['name'])
			mount = '--mount type=bind,source='+Core.path+'container/share,destination=/share'
			mount = mount + ' --mount type=bind,source=/etc/hosts,destination=/etc/hosts.main'
			run = ['--replicas ' + str(param['index']), '--name='+param['name'], '--hostname='+param['name'], mount, '--env HOSTIP="'+Core.ip()+'"']

			args = Swarm.args()
			for key in args:
				if args[key] != '':
					value = Cluster.param(param['config'], key, args[key], param['name'])
					if value != '':
						if '--mount' in value and ':' in value:
							value = value.replace(' /', '/')
							value = value.replace(':', ',destination=')
						run.append(value)

			run.append(Cluster.storeHost + param['config']['image'])

			if command == '' and 'command' in args:
				value = Cluster.param(param['config'], 'command', args['command'], param['name'])
				command = value

			if command != '':
				run.append(command)

			command = ' '.join(run)
			if 'test' in param:
				return 'docker service create ' + command
			print 'setuping ' + param['name'] + ', please wait...'
			method = Core.getMethod(Swarm, param['action'])
			method(command)
			Alias.add(param['config'], param['name'], 'docker run ' + command, param['action'], True)
			Cluster.hook('end', param['config'], param['name'])
		else:
			print param['name'] + ' cluster is setuped'

	@staticmethod
	def setting():
		ip = Args.name
		if not ip:
			ip = Core.ip()
		ckey = Args.param
		if ckey:
			Env.cluster(ckey)
		ckey = Env.cluster()
		if not ckey:
			ckey = 'dm_cluster'
			Env.cluster(ckey)
		return (ip, ckey)

	@classmethod
	def put(self, key = '', value = '', ip = '', p = True):
		if not ip:
			ip = Core.ip()
		ip = Core.ip()
		if not key:
			key = Args.name
		if not value:
			value = Args.param
		url = 'http://' + ip + ':8500/v1/kv/' + key
		Core.popen('curl -X PUT -d "'+value+'" ' + url, bg=True)
		if p == True:
			print True
		return True

	@classmethod
	def get(self, key = '', ip = '', p = True):
		if not ip:
			ip = Core.ip()
		if not key:
			key = Args.name
		import json
		import base64
		url = 'http://' + ip + ':8500/v1/kv/' + key
		value = Core.curl(url)
		if not value:
			print False
			return False
		value = json.loads(value)
		value = base64.b64decode(value[0]['Value'])
		if p == True:
			print value
		return value

	@classmethod
	def init(self, **param):
		(ip, ckey) = self.setting()
		token = Swarm.init(ip)
		print 'init cluster ...'
		if token and '--token' in token:
			Core.popen('dm pull consul')
			Core.popen('ds run daemon-master')

			token = token.split('docker swarm join --token ')
			token = token[1].split("\n")
			token = token[0].replace(' ', ':')
			data = token.split(':')
			ip = data[1]

			self.put(ckey, token, p = False)
			#Core.popen('consul kv put ' + ckey + ' ' + token)
		print 'init cluster success! please remember the ip address:'+ip+''

	@classmethod
	def join(self, **param):
		(ip, ckey) = self.setting()
		value = self.get(ckey, ip, False)
		config = value.split(':')
		print config

		'''
		Core.popen('dm pull consul')
		Swarm.join(config[0])

		Core.popen('dm run daemon-client')

		print 'join cluster:yes'
		'''
			

class Swarm(object):
	@staticmethod
	def leave():
		result = Core.shell('docker.leave')
		return result
	@staticmethod
	def name(name):
		result = Core.shell('docker.name ' + name)
		return result
	@staticmethod
	def run(command):
		#command = 'container.run ' + command
		#Core.shell(command, True, bg=False)
		command = 'docker service create ' + command
		Core.popen(command, True, bg=True)
		return command
	@staticmethod
	def show(name=''):
		print Core.shell('swarm.show ' + name)
	@staticmethod
	def args():
		return {
			'port' : '-p'
			,'volumes' : '--mount type=bind,source='
			,'environment' : '-e'
			,'command' : ''
			,'entrypoint' : '--entrypoint'
			,'network' : '--network'
			,'host' : '--add-host'
			,'root' : '--privileged='
			,'memory' : '--limit-memory='
			,'expose' : '--expose',
		}
	@staticmethod
	def drop():
		Core.shell('swarm.drop', bg=True)
	@staticmethod
	def node():
		print Core.shell('swarm.node')
	@staticmethod
	def stop(name):
		Core.shell('swarm.stop ' + name)
	@staticmethod
	def logs(name):
		Core.shell('swarm.logs ' + name, True)
	@staticmethod
	def inspect(name):
		Core.shell('swarm.inspect ' + name, True)
	@staticmethod
	def restart(name):
		return False
	@classmethod
	def delete(self, name='', bg=False):
		if name != '':
			print 'rm ' + name + ', please wait...'
			if self.check(name) == 1:
				Core.shell('swarm.rm ' + name, False, bg=bg)
		else:
			Core.shell('swarm.rm', False)
			
	@staticmethod
	def check(name):
		result = int(Core.popen('docker service ls | grep '+name+' | wc -l'))
		if result != 0:
			return 1
		else:
			return 0
	@staticmethod
	def network(self, config):
		if 'network' in config:
			name = 'overlay'
			# swarm 的 overlay网络，如果想用普通的docker run也能使用，必须加上attachable
			driver = '--driver=' + name + ' --attachable '
			if 'overlay' not in config['network']:
				config['network'] = name + '_' + config['network']
			self.conf['base']['network'] = config['network']

			result = int(Core.popen('docker network ls | grep ' + config['network'] + ' | wc -l'))
			if result == 0:
				if 'subnet' in config:
					driver = driver + ' --subnet=' + config['subnet']
				Core.shell('docker.network ' + driver + ' ' + config['network'], True)
	@staticmethod
	def save(tar, name, backup):
		return Container.save(tar, name, backup)
	@classmethod
	def load(self, tar, name):
		Container.save(tar, name)
		self.delete(name)

	@staticmethod
	def init(ip):
		result = Core.shell('swarm.token')
		if '--token' not in result:
			result = Core.shell('swarm.init ' + ip)
		return result
	@staticmethod
	def join(token, ip):
		Core.shell('swarm.join ' + token + ' ' + ip, bg=True)

	@staticmethod
	def scale(name, num):
		Core.shell('swarm.scale ' + name + '=' + num, bg=True)