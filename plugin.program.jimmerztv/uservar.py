import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Jimmerz-Wizard'
BUILDERNAME    = 'JimmerzTV'
EXCLUDES       = [ADDON_ID, 'roms', 'My_Builds', 'backupdir']
BUILDFILE      = 'http://pastebin.com/raw/DzBQ4Dyy'
UPDATECHECK    = 0
APKFILE        = 'http://pastebin.com/raw/WcjUpb5t'
YOUTUBETITLE   = 'JTV Help Videos' 
YOUTUBEFILE    = 'http://pastebin.com/raw/cf0Hwdje'
ADDONFILE      = 'http://pastebin.com/raw/q3u47MKg'
ADVANCEDFILE   = 'http://'
ROMPACK        = 'http://pastebin.com/raw/V2x4S1m8'
EMUAPKS        = 'http://pastebin.com/raw/4Dpp0JUL'
ADDONPACK      = 'http://pastebin.com/raw/V7HaYr4T'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://i.imgur.com/LoleSD8.jpg'
ICONMAINT      = 'https://i.imgur.com/LoleSD8.jpg'
ICONAPK        = 'https://i.imgur.com/LoleSD8.jpg'
ICONADDONS     = 'https://i.imgur.com/LoleSD8.jpg'
ICONYOUTUBE    = 'https://i.imgur.com/LoleSD8.jpg'
ICONSAVE       = 'https://i.imgur.com/LoleSD8.jpg'
ICONTRAKT      = 'https://i.imgur.com/LoleSD8.jpg'
ICONREAL       = 'https://i.imgur.com/LoleSD8.jpg'
ICONLOGIN      = 'https://i.imgur.com/LoleSD8.jpg'
ICONCONTACT    = 'https://i.imgur.com/LoleSD8.jpg'
ICONSETTINGS   = 'https://i.imgur.com/LoleSD8.jpg'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '~'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'ghostwhite'
COLOR2         = 'red'
COLOR3         = 'ghostwhite'
COLOR4         = 'snow'
COLOR5         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Jimmerz TV Wizard .\r\n\r\nContact us on facebook at: \r\nhttps://www.facebook.com/JimmerzElectronics/'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'icon.png')
CONTACTFANART  = 'https://i.imgur.com/FSNzrIP.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://pastebin.com/raw/MkUDM69u'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font13'
HEADERMESSAGE  = 'JTV Messages'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = 'https://i.imgur.com/FSNzrIP.jpg'
############################    #############################