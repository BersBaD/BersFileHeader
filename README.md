# Description

BersFileHeader is a plugin of Sublime Text2 which helps to add file header like

      {
        #!/usr/bin/env python
        # -*- coding:utf-8 -*-
        #############################################################################
        # ScriptName  : filename.py
        # Author      : Your name here <Your email here>
        # Create Date : 05-03-2013 12:59:42
        # Modify Date : 05-03-2013 12:59:50
        # Decription  :
        #############################################################################
      }

to your new created file, and you could define the header for yourself. Currently the plugin support python and shell, which is my mostly used.

# Installation

* The easiest way to install BersFileHeader is via the excellent Package Control Plugin
    * **NOTE** at the time of writing this, it's not in the default Package Control channel. Please add it via
        1. Open up the command palette
        2. Select "Package Control: Add Repository"
        3. Type https://github.com/BersBaD/BersFileHeader
    1. See the [Package Control Installation Instructions](http://wbond.net/sublime_packages/package_control/installation)
    2. Once package control has been installed, bring up the command palette (cmd+shift+P or ctrl+shift+P)
    3. Type Install and select "Package Control: Install Package"
    4. Select PlatformSettings from the list. Package Control will keep it automatically updated for you
* If you don't want to use package control, you can manually install it
    1. Go to your packages directory and type:
    2.    git clone https://github.com/BersBaD/BersFileHeader

# Usage

You could put settings below by click "Perferences"=>"Package Settings"=>"BersFileHeader"=>"Settings – User":

        {
            "BersFileHeader":
            {
                "add_on_created": true,
                "author": "Bers",
                "email": "bers@elite-copr.ru",
                "file_header_format": "#############################################################################\n# ScriptName  : \n# Author      : @@author <@@email>\n# Create Date :\n# Modify Date :\n# Decription  :\n#############################################################################\n",
                "file_header_format.c": "/*********************************************************#\n# ScriptName  : \n# Author      : @@author <@@email>\n# Create Date :\n# Modify Date :\n# Decription  :\n#*********************************************************/",
                "file_header_format.php": "/*********************************************************#\n# ScriptName  : \n# Author      : @@author <@@email>\n# Create Date :\n# Modify Date :\n# Decription  :\n#*********************************************************/",
                "file_header_format.pl": "#############################################################################\n# ScriptName  : \n# Author      : @@author <@@email>\n# Create Date :\n# Modify Date :\n# Decription  :\n#############################################################################\n",
                "file_header_format.sh": "#############################################################################\n# ScriptName  : \n# Author      : @@author <@@email>\n# Create Date :\n# Modify Date :\n# Decription  :\n#############################################################################\n",
                "ignore_files":
                [
                    ".*.sublime.*",
                    "README",
                    ".*.sublime-settings",
                ],
                "perl": "#!/usr/bin/env perl -w",
                "python": "#!/usr/bin/env python\n# -*- coding:utf-8 -*-",
                "shell": "#!/usr/bin/env bash",
                "time_format": "%d-%m-%Y %H:%M:%S"
            }
        }



# Features
* Modify Date will change each time you save(CTRL+S) the file
* ScriptName will change each time you save as(CTRL+SHIFT+S) the file
* CTRL+SHIFT+H could add defined header to your current file which has no header
* Custom time format, using Python datetime format, please refer to https://github.com/BersBaD/BersFileHeader/blob/master/time_format.md
* CTRL+SHIFT+H will use file ctime as Create Date for existed file
* You could set add_on_created to false so that when file is created, the header won't be added automatically(set this to be false if you want to use multiple header formats functions now)
* Multiple header formats such as(but add_on_created should be set to false now):

        "BersFileHeader"{
            "file_header_format.c":"xxxxxxx"
            "file_header_format.php": "/**/"
            "file_header_format.py": "#######"
        }
