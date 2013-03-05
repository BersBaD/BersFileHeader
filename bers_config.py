#!/usr/bin/env python
# -*- coding:utf-8 -*-
#############################################################################
# ScriptName  : bers_config.py
# Author      : Bers <bers@elite-copr.ru>
# Create Date : 05-03-2013 14:13:55
# Modify Date : 05-03-2013 14:26:13
# Decription  :
#############################################################################
import sublime


class BersConfig:

    config = None

    @classmethod
    def get_singleton(self):
        self.load_settings()

        return self.config

    @classmethod
    def load_settings(self):
        s = sublime.load_settings('Preferences.sublime-settings')
        self.config = s.get('bers_file_header')
        if not self.config:
            raise Exception("bers_file_header is not configured.")

        print self.config
        """set default time_format"""
        if not self.config.get('time_format'):
            self.config['time_format'] = '%d-%m-%Y %H:%M:%S'
