#!/usr/bin/env python
# -*- coding:utf-8 -*-
#############################################################################
# ScriptName  : BersFileHeader.py
# Author      : Bers <bers@elite-copr.ru>
# Create Date : 24-07-2014 16:16:17
# Modify Date : 24-07-2014 16:30:17
# Decription  :
#############################################################################

import sublime
import sublime_plugin
import os
import datetime
import re

# from BersConfig import BersConfig

class BersConfig:

    config = None

    @classmethod
    def get_singleton(self):
        self.load_settings()
        return self.config

    @classmethod
    def load_settings(self):
        s = sublime.load_settings('BersFileHeader.sublime-settings')
        self.config = s.get('BersFileHeader')
        if not self.config:
            raise Exception("BersFileHeader is not configured.")

        """set default time_format"""
        if not self.config.get('time_format'):
            self.config['time_format'] = '%d-%m-%Y %H:%M:%S'

class BersAddHeaderOnCreatedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        bers_config = BersConfig.get_singleton()
        if bers_config.get('add_on_created') == False:
            return
        else:
            self.view.run_command('bers_file_new_header')

class BersFileNewHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        bers_config = BersConfig.get_singleton()
        if not self.view.file_name():
            file_header_format = bers_config.get('file_header_format')
        else:
            file_name = self.view.file_name()
            prefix, extensions = os.path.splitext(file_name)
            file_header_format = bers_config.get('file_header_format' + extensions)
            if not file_header_format:
                file_header_format = bers_config.get('file_header_format')

        """replace @@author and @@email with the user definied value"""
        author = bers_config.get('author')
        email = bers_config.get('email')
        file_header_format = file_header_format.replace('@@author', author)
        file_header_format = file_header_format.replace('@@email', email)

        """
            when file exists already, we need to use original create time
            using os.stat, otherwise using current time instead
        """
        if not self.view.file_name():
            create_time = datetime.datetime.now().strftime(bers_config.get('time_format'))
        else:
            file_stat = os.stat(self.view.file_name())
            st_ctime = file_stat[9]
            create_time = datetime.datetime.fromtimestamp(st_ctime).strftime(bers_config.get('time_format'))
        if file_header_format.find('Create Date') >= 0:
            file_header_format = file_header_format.replace('Create Date :', 'Create Date : ' + create_time)

        self.view.insert(edit, 0, file_header_format)

class BersAddCmdHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        bers_config = BersConfig.get_singleton()
        if bers_config.get('add_on_created') == False:
            return

        file_name = self.view.file_name()
        if file_name.endswith('.py'):
            cmd_header = bers_config.get('python')
        elif file_name.endswith('.sh'):
            cmd_header = bers_config.get('shell')
        elif file_name.endswith('.pl'):
            cmd_header = bers_config.get('perl')

        cmd_headers = cmd_header.split('\n')
        exists = False
        for line_no in xrange(0, 5):
            line = self.view.substr(self.view.line(line_no))
            for cmd_line in cmd_headers:
                if line.find(cmd_line) >= 0:
                    exists = True
                    break

        if not exists:
            self.view.insert(edit, 0, cmd_header + '\n')

class BersAddFileFooterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        default_footer = os.linesep
        """add a line to the end of the line"""
        last_line = self.view.substr(self.view.line(self.view.size()))
        if len(last_line) > 0:
            self.view.insert(edit, self.view.size(), default_footer)

class BersFileModifiedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        modified_date_region = self.view.find('Modify Date', 0)
        if modified_date_region:
            line = self.view.line(modified_date_region)
            now = datetime.datetime.now().strftime(BersConfig.get_singleton().get('time_format'))
            string_line = self.view.substr(line)
            before_pos = string_line.find('Modify Date')
            before_string = ''
            if before_pos >= 0:
                before_string = string_line[0:before_pos]
            self.view.replace(edit,
                              line,
                              before_string + 'Modify Date : ' + now)

        file_name_region = self.view.find('ScriptName', 0)
        if file_name_region:
            line = self.view.line(file_name_region)
            string_line = self.view.substr(line)
            before_pos = string_line.find('ScriptName')
            before_string = ''
            if before_pos >= 0:
                before_string = string_line[0:before_pos]
            self.view.replace(edit,
                              line,
                              before_string + 'ScriptName  : ' + os.path.basename(self.view.file_name()))

class BersAddFileHeaderManually(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('bers_file_new_header')
        self.view.run_command('bers_file_modified')
        self.view.run_command('bers_add_cmd_header')

class BersAddFileAndCmdHeader(sublime_plugin.EventListener):
    def on_new(self, view):
        view.run_command('bers_add_header_on_created')

    def on_pre_save(self, view):
        bers_config = BersConfig.get_singleton()
        ignore_files = bers_config.get('ignore_files')
        current_file = os.path.basename(view.file_name())
        for f in ignore_files:
            pattern = re.compile(f)
            if pattern.match(current_file):
                return

        view.run_command('bers_file_modified')
        view.run_command('bers_add_cmd_header')
        view.run_command('bers_add_file_footer')
