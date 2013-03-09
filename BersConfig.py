#!/usr/bin/env python
# -*- coding:utf-8 -*-
#############################################################################
# ScriptName  : BersConfig.py
# Author      : Bers <bers@elite-copr.ru>
# Create Date : 06-03-2013 00:09:04
# Modify Date : 06-03-2013 00:59:49
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
        s = sublime.load_settings('BersFileHeader.sublime-settings')
        self.config = s.get('BersFileHeader')
        if not self.config:
            raise Exception("BersFileHeader is not configured.")

        print self.config
        """set default time_format"""
        if not self.config.get('time_format'):
            self.config['time_format'] = '%d-%m-%Y %H:%M:%S'
