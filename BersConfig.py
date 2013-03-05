#!/usr/bin/env python
# -*- coding:utf-8 -*-
#############################################################################
# ScriptName  : BersConfig.py
# Author      : Bers <bers@elite-copr.ru>
# Create Date : 05-03-2013 19:31:34
# Modify Date : 05-03-2013 23:29:55
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
        # s = sublime.load_settings('Preferences.sublime-settings')
        s = sublime.load_settings('BersFileHeader.sublime-settings')
        self.config = s.get('BersFileHeader')
        if not self.config:
            raise Exception("BersFileHeader is not configured.")

        print self.config
        """set default time_format"""
        if not self.config.get('time_format'):
            self.config['time_format'] = '%d-%m-%Y %H:%M:%S'
