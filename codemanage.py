#-*- coding: UTF-8 -*-
import sublime, sublime_plugin
import os
import os.path
import time

#写入模板，如果是新模板按照模板名创建一个文件，如果是旧模板则覆盖写原文件
class CodeTplAddCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		#获取当前选中内容
		selstr = ''
		sels = self.view.sel()
		for sel in sels:
			value = self.view.substr(sel)
			if value == '':
				continue
			selstr = selstr + value + '\n'

		if selstr == '':
			sublime.message_dialog("Select content is empty.")
			return

		def on_done(name):
			if name=='':
				sublime.message_dialog("Template name is empty.")
				return
			#写入文件
			path = os.path.join(sublime.packages_path(),"CodeManage","template",name+".ctpl")
			try:
				f = open(path, 'w')
				f.write(selstr)
			except Exception, e:
				sublime.message_dialog("Write template file fail:"+str(e))
				return
			finally:
				f.close()

		def on_change(name):
			return

		def on_cancel():
			return

		#输入模板名
		self.view.window().show_input_panel('Plese input the code template name','template',on_done,on_change,on_cancel)

#将对应模板插入当前位置
class CodeTplInsertCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		filenames = []
		rootdir= os.path.join(sublime.packages_path(),"CodeManage","template")
		for p,d,files in os.walk(rootdir):
			filenames = files

		def on_sel_done(selvalue):
			if selvalue==-1:
				return
			filename = filenames[selvalue]
			content = ''

			if filename=='':
				sublime.message_dialog("Template is not exist.")
				return
			path = os.path.join(sublime.packages_path(),"CodeManage","template",filename)

			try:
				f =  open(path, 'r')
				content = f.read()
				if content=='':
					sublime.message_dialog("Template file is empty")
					return
				content = ReplaceVar(content)
			except Exception, e:
				sublime.message_dialog("Open template file fail:"+str(e))
				return
			finally:
				f.close()
			
			#把内容插入当前位置
			sels = self.view.sel()
			for sel in sels:
				self.view.insert(edit,sel.begin(),content)

		#打开选择列表
		self.view.window().show_quick_panel(filenames,on_sel_done)

#处理一些模板替换变量
#将模板中{{XXX}}的变量替换成配置文件中的变量({{data}}等信息直接替换)
def ReplaceVar(content):
	varmap = {
		'{{date}}':time.strftime('%Y-%m-%d',time.localtime(time.time()))
	}
	#读取变量
	try:
		path = os.path.join(sublime.packages_path(),"CodeManage","var-map.conf")
		f =  open(path, 'r')
		for line in f.readlines():
			if line=='':
				continue
			value = line.split("=")
			varmap["{{"+value[0]+"}}"] = value[1]
	except Exception, e:
		sublime.message_dialog("Open var-map file fail:"+str(e))
		return
	finally:
		f.close()
	
	for (k,v) in varmap.items():
		content = content.replace(k,v)
	return content