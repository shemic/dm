#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:docker.py
    author:rabin
"""
from dever import *

class Docker(object):
	path = 'src/docker/'
	default = 'shemic'
	@classmethod
	def init(self):
		self.conf = {}
		self.core = Config.core(self.path)
		self.store = Env.store()
		self.storeHost = self.core['store'][self.store] + '/'

		action = ('uprun', 'run', 'rm', 'rmb', 'stop', 'create', 'call', 'save', 'load', 'show', 'reset', 'logs', 'restart', 'inspect', 'test')
		method = Dever.getMethod(Docker_Action, Args.action)
		if Args.name and Args.action in action:
			self.load(method)
		else:
			method()

	@classmethod
	def load(self, method):
		self.config()
		Container.network(self.conf['base'])
		self.rely(self.conf['base'], Args.action)
		one = False
		if Args.index in self.conf['config']:
			self.handle(method, self.conf['config'][Args.index], Args.index, Args.action)
		else:
			for item in self.conf['server']:
				if self.check(Args.index, item) == True:
					self.handle(method, self.conf['config'][item], item, Args.action)
	@classmethod
	def config(self):
		if not self.conf:
			self.conf = Config.read(self.path)

	@classmethod
	def check(self, name, item):
		if '#' in item:
			return False
		elif name == '':
			return True
		elif name + '-' in item:
			return True
		else:
			return False

	@classmethod
	def handle(self, method, config, item, action='run'):
		self.rely(config, action)
		if 'num' not in config:
			config['num'] = 1
		num = int(config['num'])
		i = 1;
		while (i <= num):
			name = self.name(item, i)
			if 'image' not in config:
				config['image'] = item
			if self.store == 'private' and config['image'] in self.core['images']:
				config['image'] = self.core['images'][config['image']]
			method(config=config, name=name, item=item, index=i, action=action)
			if action in ('stop', 'restart', 'rm', 'rmb', 'reset', 'run', 'create'):
				self.slave(config, item, action)
			i = i + 1

	@classmethod
	def name(self, name, i):
		name = Args.name + '-' + name
		if i > 1:
			self.conf['base']['i'] = '' + str(i)
			i = i - 1;
			self.conf['base']['num'] = '' + str(i)
			return name + self.conf['base']['num'];

		self.conf['base']['num'] = ''
		self.conf['base']['i'] = '1'
		return name;

	@classmethod
	def param(self, config, item, prefix, name):
		result = ''
		concat = ' '
		if item in config:
			if '#' not in item:
				result = config[item]
				if '[' in config[item]:
					search = re.search(r'\[(.*?)\]', result, re.M|re.I)
					temp = search.group(1)
					if temp:
						result = Dever.replace('['+str(temp)+']', self.name(temp, 1), result)
				result = Dever.replace('{num}', self.conf['base']['num'], result)
				result = Dever.replace('{i}', self.conf['base']['i'], result)
				result = Dever.replace('{path}', self.conf['base']['path'], result)
				result = Dever.replace('{container}', self.conf['base']['path'] + 'container/', result)
				result = Dever.replace('{name}', name, result)
				result = self.parse(result)
				result = Dever.replace(',', ' ' + prefix + ' ', result)
				if item == 'hostname':
					name = result

		elif item == 'network' and 'network' in self.conf['base']:
			result = self.conf['base']['network']

		if result != '':
			if '=' in prefix:
				concat = ''
			result = prefix + concat + result

		return result

	@classmethod
	def parse(self, result):
		if '{$' in result:
			param = {}
			if Args.param != '':
				if 'http://' not in Args.param:
					Args.param = 'http://shemic.com/?' + Args.param;
				if '^' in Args.param:
					Args.param = Dever.replace('^', '&', Args.param)
				parse = urlparse.urlparse(Args.param)
				param = urlparse.parse_qs(parse.query,True)

			search = re.compile(r'\{\$(.*?)\}')
			search = search.findall(result)
			for key in search:
				value = ''
				index = key
				if ':' in key:
					arr = key.split(':');
					index = arr[0]
					value = arr[1]
				if index in param:
					value = param[index][0]
				if value == '':
					print 'please set param value:' + index
					sys.exit()
				else:
					result = Dever.replace('{$'+key+'}', value, result)
		return result

	@classmethod
	def rely(self, config, action):
		if 'rely' in config:
			if ',' in config['rely']:
				rely = config['rely'].split(',');
				for i in rely:
					Dever.popen('dever ' + action + ' ' + i, True)
			else:
				Dever.popen('dever ' + action + ' ' + config['rely'], True)

	@classmethod
	def hook(self, type, config, name):
		key = 'hook.'+type
		if key in config:
			Dever.shell('hook.' + config[key] + ' ' + name + ' ' + Dever.path, bg=True)

	@classmethod
	def slave(self, config, name, action):
		if 'slave' in config:
			i = 1
			num = int(config['slave'])
			key = ['slave', 'command', 'alias', 'port', 'hook.start', 'hook.end']
			for k in key:
				if k in config:
					del config[k]
			while (i <= num):
				self.runServerOne(config, name + '-slave', i, action)
				i = i + 1
	@classmethod
	def tar(self, name):
		path = Dever.path + 'data/backup/' + name + '/'
		File.mkdir(path)
		backup = 'backup/' + name
		tar = path + name + '.tar'
		return tar,backup

class Docker_Action(object):
	@staticmethod
	def build():
		if Args.name and Args.name in Docker.core['images']:
			Args.name = Docker.core['images'][Args.name]
		Image.build(Docker.storeHost, Args.name)
		Container.delete()
		Image.delete()
		print 'docker build '+Args.name+':yes'

	@classmethod
	def push(self):
		package = self.package()
		if Args.name != '':
			if Args.name in package:
				Image.push(package[Args.name])
			else:
				print 'error ' + Args.name
			sys.exit()

		for key in package:
			Image.push(package[key])

	@classmethod
	def login(self):
		if Args.name and Args.name in Docker.core['store']:
			Dever.shell('docker.login ' + Docker.core['store'][Args.name], True)
		else:
			for key,value in Docker.core['store'].items():
				Dever.shell('docker.login ' + value, True)

	@staticmethod
	def package():
		stores = Docker.core['store']
		result = {}
		del stores[Docker.store]
		for key,value in Docker.core['images'].items():
			if Docker.store == 'private': 
				index = Docker.storeHost + value
			else:
				index = Docker.storeHost + key
			result[key] = []
			result[key].append(index)
			for k,v in stores.items():
				if k == 'private': 
					host = v + '/' + value
				else:
					host = v + '/' + key
				if host != index:
					result[key].append(host)
		if Args.name and Args.name in result:
			value = Args.name + ' [' + ",".join(result[Args.name ]) + ']'
			print value
		else:
			i = 1
			for key in result:
				value = key + ' [' + ",".join(result[key]) + ']'
				print str(i) + ':' + value
				i = i + 1
		return result

	@staticmethod
	def showi():
		Image.show()

	@staticmethod
	def rmi():
		Image.delete()
		print 'rm image:yes'

	@staticmethod
	def drop():
		Container.drop()
		print 'drop container:yes'

	@staticmethod
	def dropi():
		Image.drop(Args.name)
		print 'drop image:yes'

	@staticmethod
	def show(**param):
		name = ''
		if param:
			name = param['name']
		Container.show(name)

	@staticmethod
	def logs(**param):
		Container.logs(param['name'])

	@staticmethod
	def restart(**param):
		print 'reloading ' + param['name'] + ', please wait...'
		Container.restart(param['name'])

	@staticmethod
	def inspect(**param):
		Container.inspect(param['name'])

	@staticmethod
	def stop(**param):
		Container.stop(param['name'])

	@staticmethod
	def save(**param):
		tar,backup = Docker.tar(param['name'])
		Container.save(tar, param['name'], backup)

	@classmethod
	def load(self, **param):
		tar,backup = Docker.tar(param['name'])
		Container.load(tar, param['name'])
		Docker.storeHost = ''
		param['config']['image'] = backup
		self.run(**param)

	@classmethod
	def uprun(self, **param):
		Image.install(Docker.storeHost, param['config']['image'])
		param['action'] = 'run'
		self.run(**param)

	@staticmethod
	def rm(**param):
		if param and 'name' in param:
			Container.delete(param['name'])
			Alias.delete(param['config'], param['name'])
		else:
			Container.delete()
			print 'rm container:yes'

	@staticmethod
	def rmb(**param):
		if param and 'name' in param:
			Container.delete(param['name'], bg=True)
			Alias.delete(param['config'], param['name'])
		else:
			Container.delete()
			print 'rm container:yes'

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
		daemon = '-d'
		restart = '--restart=always'
		if 'daemon' in param['config']:
			daemon = param['config']['daemon']
			if daemon == 'false':
				daemon = ''
				restart = ''

		if 'image' not in param['config']:
			param['config']['image'] = ''
		if 'restart' in param['config']:
			restart = ''

		if param['action'] == 'call':
			runCommand = Docker.param(param['config'], 'call', '', param['name'])
			command = Docker.param(param['config'], 'param', '', param['name'])
			restart = '--entrypoint' + runCommand
			daemon = '--rm'
			param['action'] = 'run'

		state = Container.check(param['name'])
		if state == 0:
			Docker.hook('start', param['config'], param['name'])
			run = ['-it', '--name='+param['name'], '--hostname='+param['name'], restart, daemon, '-v '+Dever.path+'container/share:/share -v /etc/hosts:/etc/hosts.main']

			args = Container.args()
			for key in args:
				if args[key] != '':
					value = Docker.param(param['config'], key, args[key], param['name'])
					if value != '':
						run.append(value)

			run.append(Docker.storeHost + param['config']['image'])

			if command == '' and 'command' in args:
				value = Docker.param(param['config'], 'command', args['command'], param['name'])
				command = value

			if command != '':
				run.append(command)

			command = ' '.join(run)
			if 'test' in param:
				return 'docker run ' + command
			print 'setuping ' + param['name'] + ', please wait...'
			method = Dever.getMethod(Container, param['action'])
			method(command)
			Alias.add(param['config'], param['name'], 'docker run ' + command, param['action'])
			Docker.hook('end', param['config'], param['name'])
		else:
			self.restart(**param)

class Container(object):
	@staticmethod
	def run(command):
		command = 'container.run ' + command
		Dever.shell(command, True, bg=False)
		return command
	@staticmethod
	def show(name=''):
		print Dever.shell('container.show ' + name)
	@staticmethod
	def args():
		return {
			'port' : '-p'
			,'volumes' : '-v'
			,'environment' : '-e'
			,'link' : '--link'
			,'volumes_from' : '--volumes-from'
			,'command' : ''
			,'entrypoint' : '--entrypoint'
			,'network' : '--net='
			,'host' : '--add-host'
			,'root' : '--privileged='
			,'memory' : '--memory='
			,'expose' : '--expose',
		}
	@staticmethod
	def drop():
		Dever.shell('container.drop', bg=True)
	@staticmethod
	def stop(name):
		Dever.shell('container.stop ' + name)
	@staticmethod
	def logs(name):
		Dever.shell('container.logs ' + name, True)
	@staticmethod
	def inspect(name):
		Dever.shell('container.inspect ' + name, True)
	@staticmethod
	def restart(name):
		Dever.shell('container.restart ' + name)
	@classmethod
	def delete(self, name='', bg=False):
		if name != '':
			print 'rm ' + name + ', please wait...'
			if self.check(name) == 1:
				Dever.shell('container.rm ' + name, False, bg=bg)
		else:
			Dever.shell('container.rm', False)
			
	@staticmethod
	def check(name):
		result = int(Dever.popen('docker ps -a | grep '+name+' | wc -l'))
		if result != 0:
			return 1
		else:
			return 0
	@staticmethod
	def network(config):
		if 'network' in config:
			result = int(Dever.popen('docker network ls | grep ' + config['network'] + ' | wc -l'))
			if result == 0:
				Dever.shell('container.network ' + config['network'], True)
	@staticmethod
	def save(tar, name, backup):
		if File.exists(tar) == True:
			now = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
			old = replace('.tar', '.' + now + '.tar', tar)
			File.rename(tar, old)
		Dever.popen('docker commit -p ' + name + ' ' + backup)
		Dever.popen('docker save ' + backup + ' > ' + tar, True)
	@classmethod
	def load(self, tar, name):
		Dever.popen('docker load < ' + tar, True)
		self.delete(name)

class Image(object):
	@classmethod
	def push(self, stores):
		store = stores[0]
		if self.check(store) == 1:
			del stores[0]
			Dever.shell('image.push ' + store, bg=True)
			for value in stores:
				#print store + ' ' + value
				Dever.shell('image.push ' + store + ' ' + value, bg=True)
	@staticmethod
	def show():
		print Dever.shell('image.show')
	@staticmethod
	def drop(name=''):
		Dever.shell('image.drop ' + name, bg=True)
	@staticmethod
	def delete():
		Dever.shell('image.rm', bg=True)
	@staticmethod
	def build(path, name):
		file = Dever.path + Docker.path + 'build/' + name + '/'
		name = path + name
		Dever.shell('image.build ' + name + ' ' + file, True)
	@staticmethod
	def check(name):
		result = int(Dever.popen('docker images | grep '+name+' | wc -l'))
		if result != 0:
			return 1
		else:
			return 0
	@staticmethod
	def install(library, key):
		pull = 'docker pull';
		command = pull + ' ' + library + key
		Dever.popen(command, True)
		print 'finished'