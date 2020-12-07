from kivy.config import Config
Config.set('graphics', 'borderless', '0')
Config.set('graphics', 'resizable', 'True')
Config.set('kivy','window_icon','[pic_control\\icon.ico')

Config.set('graphics', 'multisamples', '0')

from kivy.app import App
import kivy
kivy.require('1.11.1')
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen,SwapTransition,\
    FadeTransition,WipeTransition,FallOutTransition,RiseInTransition,\
    CardTransition,SlideTransition, NoTransition
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.properties import ObjectProperty,NumericProperty,\
     BooleanProperty,StringProperty,ListProperty,OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView,DampedScrollEffect
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.stencilview import StencilView
from kivy.uix.bubble import Bubble
from kivy.uix.modalview import ModalView


from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Rectangle,Color,Triangle,Line

from HoverBehavior import HoverBehavior
from dialog import MDDialog
#from button import Button
#from card import MDSeparator
#from kivymd.date_picker import MDDatePicker
from menu import MDDropdownMenu
from ripplebehavior import CircularRippleBehavior,RectangularRippleBehavior

import datepicker

from functools import partial
import threading
from kivy.clock import mainthread
import requests
from isbntools import *
from isbntools.app import goom

import datetime
import isbnlib
import os
import glob
import sqlite3
import secrets
import shutil,errno
import reportlab
import matplotlib.pyplot as plt
from winreg import *
import ast
import socket
import urllib
import re
from kivy.graphics.instructions import InstructionGroup
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.popup import Popup
import tempfile
import win32api
import win32print
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39
import subprocess
from textwrap import wrap
from kivy.core.window import Window
from PIL import ImageDraw, ImageFilter
from PIL import Image as Mage
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import kivy.properties as props

from kivy.graphics.texture import Texture
from kivy.uix.behaviors import ButtonBehavior
from PIL import ImageDraw, ImageFilter
from PIL import Image as Imgpil
import kivy.properties as props
import pyscreenshot as ImageGrab
from kivy.metrics import dp
from subprocess import Popen
import pdf2image
from PyPDF2 import PdfFileReader
from navigation_drawer import NavigationDrawer


#os.startfile('C:\\Systems\\Library management system\\backup.bat')

RAD_MULT = 0.25 #  PIL GBlur seems to be stronger than Chrome's so I lower the radius

import sys, os, traceback, types

def isUserAdmin():
    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print ("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))

def runAsAdmin(cmdLine=None, wait=True):

    if os.name != 'nt':
        raise RuntimeError( "This function is only implemented on Windows.")

    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType,types.ListType):
        raise ValueError( "cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    # XXX TODO: isn't there a function or something we can call to massage command line params?
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    #showCmd = win32con.SW_HIDE
    lpVerb = 'runas'  # causes UAC elevation prompt.

    # print "Running", cmd, params

    # ShellExecute() doesn't seem to allow us to fetch the PID or handle
    # of the process, so we can't get anything useful from it. Therefore
    # the more complex ShellExecuteEx() must be used.

    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']    
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
        #print "Process handle %s returned code %s" % (procHandle, rc)
    else:
        rc = None

    return rc
def test():
    rc = 0
    if not isUserAdmin():
        print ("You're not an admin.", os.getpid(), "params: ", sys.argv)
        #rc = runAsAdmin(["c:\\Windows\\notepad.exe"])
        rc = runAsAdmin()
    else:
        print ("You are an admin!", os.getpid(), "params: ", sys.argv)
        rc = 0
    return rc
##
#test()

class BoxWhite(BoxLayout):
    pass

class MDSeparator(BoxLayout):
    color = ListProperty([0,0,0,.15])
    """ A separator line """
    def __init__(self, *args, **kwargs):
        super(MDSeparator, self).__init__(*args, **kwargs)
        self.on_orientation()
    
    def on_orientation(self,*args):
        self.size_hint = (1, None) if self.orientation == 'horizontal' else (None, 1)
        if self.orientation == 'horizontal':
            self.height = (1)
        else:
            self.width = (1)
            
class MDLabel(Label):
    font_style = OptionProperty(
        'Caption', options=['Caption', 'Subhead', 'Title','Body2','Headline'])
    def __init__(self, **kwargs):
        super(MDLabel, self).__init__(**kwargs)
        
class MaterialWidget(ButtonBehavior, BoxLayout):
    elevation = NumericProperty(1)
    theme = BooleanProperty(False)

    def __init__(self,**kwargs):
        super(MaterialWidget, self).__init__(**kwargs)
        
    

class ButtonBase(ButtonBehavior, Label):
    pass
    
class IconButton(CircularRippleBehavior, ButtonBase):
    icon = StringProperty()
    
class TextField(TextInput):
    pass

class TextFieldM(MaterialWidget):
    text = StringProperty()
    hint_text = StringProperty()


class Ripplebtn(RectangularRippleBehavior, MDLabel):
    pass


class HoverTool(ToggleButtonBehavior, BoxLayout):
    def on_state(self, inst,value):
        if value =='down':
            anim =Animation(width =dp(230), t = 'in_cubic', duration =.3)
            anim.start(self)
        else:
            anim =Animation(width =dp(60), t = 'out_cubic', duration =.3)
            anim.start(self)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            self.state = 'normal'
        else:
            return super(HoverTool, self).on_touch_down(touch)
    
class CointainerHeaders(ToggleButtonBehavior, BoxLayout):
    list_widgets = ListProperty('')
    icon = StringProperty()
    text = StringProperty()
    icon1 = StringProperty(u'\uF140')
    color = ListProperty([0,0,0,.83])

    def __init__(self, **kwargs):
        super(CointainerHeaders, self).__init__(**kwargs)

        
    def on_state(self, inst,value):
        print(value)
        if value =='down':
            self.show()
            self.icon1 = u'\uF143'
            self.parent.parent.parent.state ='down'
         
        else:
            self.unshow()
            self.icon1 = u'\uF140'

    def on_size(self, *args):
        try:
            self.ids.sm_main.transition = NoTransition()
            
            if self.width < dp(220):
                self.ids.sm_main.current = 'one'
                
            elif self.width > dp(220):
                self.ids.sm_main.current = 'two'
        except:
            pass
            
    def show(self):
        self.color = 0, 52/255, 102/255, 1
        for wid in self.list_widgets:
            wid.halign = 'left'
            wid.padding_x=dp(56)
            wid.shorten=True
            wid.shorten_from ='right'
            self.add_widget(wid, state='new')
            self.height +=wid.height

    def unshow(self):
        self.color =0,0,0,.83
        for wid in self.list_widgets:
            self.remove_widget(wid)
            self.height -=wid.height

    def add_widget(self, widget, index=0, state=None, canvas=None):
        if state == None and isinstance(widget, BoxLayout)==False:
            self.list_widgets.append(widget)
        else:
            return super(CointainerHeaders, self).add_widget(widget, index, canvas)

    

class TitleButtons(ToggleButtonBehavior, Ripplebtn):
    def __init__(self, **kwargs):
        super(TitleButtons, self).__init__(**kwargs)
        self.group = 'menu'
        self.size_hint = None, None
        self.height = 100
        
        
    def on_state(self, widget, state):
        if state == 'down':
            anim = Animation(rgba=(0, 52/255, 102/255, .3))
            anim.start(self.canvas.get_group('a')[0])
            self.font_style= 'Title'
            self.color =0, 52/255, 102/255, 1
        else:
            anim = Animation(rgba=(0, 52/255, 102/255, 0), t= 'out_cubic')
            anim.start(self.canvas.get_group('a')[0])
            self.font_style= 'Subhead'
            self.color = 0,0,0,1
        

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Pop(Popup):
    popup_back_color = ListProperty([])
    def __init__(self,**kwargs):
        super(Pop,self).__init__(**kwargs)
        self.background=''
        self.separator_height=0
        
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class CustomTgglButton(ToggleButton):
    pass

class MDFlatButtonc(RectangularRippleBehavior, ButtonBehavior, MDLabel, HoverBehavior):
    
    def __init__(self, **kwargs):
        super(MDFlatButtonc, self).__init__(**kwargs)
    
    def on_enter(self):
        self.high = InstructionGroup()
        self.high.add(Color(0, 0, 1, 0.2))
        self.high.add(Rectangle(pos=self.pos, size=self.size))
        self.canvas.add(self.high)
    
    def on_leave(self):
        self.canvas.remove(self.high)

class Image_Theme(ToggleButtonBehavior, Image):
    def on_state(self, inst, value):
        if value == 'down':
            with self.canvas.after:
                Color(1,1,1,.5)
                Rectangle(size=self.size,pos=self.pos)
        else:
            self.canvas.after.clear()
    
class DashLabel(BoxLayout):
    lbl=ObjectProperty()
    
class AnalysisRV(MDFlatButtonc):
    def __init__(self,**kwargs):
        super(AnalysisRV,self).__init__(**kwargs)

class AnalysisRVBarcode(Label):
    def __init__(self,**kwargs):
        super(AnalysisRVBarcode,self).__init__(**kwargs)
        
class RecycleV(RecycleView):
    def __init__(self, **kwargs):
        super(RecycleV, self).__init__(**kwargs)
        
class RecycleVBarcode(RecycleView):
    def __init__(self, **kwargs):
        super(RecycleVBarcode, self).__init__(**kwargs)
        
#screenmanager notification
class ScreenMN(Carousel):
    pass
        
#notify button
class NotifyButton(MaterialWidget):
    lbl_not=ObjectProperty()
    img_s=ObjectProperty()

#no dumped effect scrollview
class Scroller(ScrollView):
    def __init__(self, **kwargs):
        super(Scroller, self).__init__(**kwargs)
        self.effect_cls=DampedScrollEffect

    
#commonCard for all widget
class CardCommon(HoverBehavior, MaterialWidget):
    
    def __init__(self,**kwargs):
        super(CardCommon, self).__init__(**kwargs)
            

    def on_enter(self):
        self.event=Clock.schedule_once(self.elevate_up,.6)     
    
    def elevate_up(self,*args):
        self.elevation= 4

    def on_leave(self):
        self.event.cancel()
        Clock.schedule_once(self.elevate_down,.6)
        
    def elevate_down(self,*args):
        self.elevation=1

#user widget
class User_widet(CardCommon, ButtonBehavior):
    username = StringProperty('')
    password = StringProperty('')
    
class AutocompleteButton(RectangularRippleBehavior, ButtonBehavior, Label):
    isbn = StringProperty('')
    title = StringProperty('')
    publisher = StringProperty('')
    edition = StringProperty('')
    author = StringProperty('')
    place_of_publication = StringProperty('')
    year_of_publication = StringProperty('')

    
#search button for borrow
class Search_Tab(CardCommon):
    txt = ObjectProperty()
    btn = ObjectProperty()
        
class Backup_restore(CardCommon):
    mdl=ObjectProperty()
    btn=ObjectProperty()
    imgb=ObjectProperty()


#notification button
class NotificationB(CardCommon):
    adm_id_lbl=ObjectProperty()
    adm_id=ObjectProperty()
    name=ObjectProperty()
    titl=ObjectProperty()
    reg_as=ObjectProperty()
    show_mem=ObjectProperty()
    date_pass=ObjectProperty()

    def __init__(self, adm_id, name, titl, reg_as, date_pass, **kwargs):
        super(NotificationB,self).__init__(**kwargs)
        if reg_as=='student':
            self.ids.adm_id_lbl.text='Admission no. :'
        else:
            self.ids.adm_id_lbl.text='Id no. :'
        self.ids.adm_id.text=str(adm_id)
        self.ids.name.text=str(name)
        self.ids.titl.text=str(titl)
        self.ids.reg_as.text=str(reg_as)
        self.ids.date_pass.text=str(date_pass)
        

class BorrowButton(CardCommon):
    gdl=ObjectProperty()
    imgb=ObjectProperty()
    acc_n=ObjectProperty()
    titl=ObjectProperty()
    publ=ObjectProperty()
    moreb=ObjectProperty()
    date_iss=ObjectProperty()
    date_supp=ObjectProperty()
    date_pass=ObjectProperty()
    ret_book=ObjectProperty()
    marklost=ObjectProperty()
    memb_reg=ObjectProperty()
    adm_id=ObjectProperty()
    pers=ObjectProperty()
    memb_serv=ObjectProperty()
    
    def __init__(self, acc, titl, publ, date_iss, date_supp, date_pas,served,mem_type='student', **kwargs):
        super(BorrowButton,self).__init__(**kwargs)
        self.ids.acc_n.text=str(acc)
        self.ids.titl.text=str(titl)
        self.ids.publ.text=str(publ)
        self.ids.date_iss.text=str(date_iss)
        self.ids.date_supp.text=str(date_supp)
        self.ids.date_pass.text=str(date_pas)
        self.ids.memb_reg.text=str(mem_type)
        self.ids.memb_serv.text=str(served)
        
class HistoryButton(CardCommon):
    gdl=ObjectProperty()
    imgb=ObjectProperty()
    acc_n=ObjectProperty()
    titl=ObjectProperty()
    publ=ObjectProperty()
    date_iss=StringProperty()
    date_ret=StringProperty()
    date_supp=StringProperty()
    date_pass=StringProperty()
    ret_book=StringProperty()
    showmore=ObjectProperty()
    
    def __init__(self, acc, titl, publ, date_iss, date_supp, date_ret, date_pas, **kwargs):
        super(HistoryButton,self).__init__(**kwargs)
        self.ids.acc_n.text=str(acc)
        self.ids.titl.text=str(titl)
        self.ids.publ.text=str(publ)
        self.date_iss=date_iss
        self.date_supp=date_supp
        self.date_ret=date_ret
        self.date_pass=date_pas

    def show_more_less(self):
        if self.ids.showmore.text=='More...':
            self.date_issue_l=Label(text='Date issued :', size_hint=(1,None),size=(1,20))
            self.date_issue_lr=MDLabel(text= self.date_iss, size_hint=(1,None),size=(1,20),halign='left')
            self.date_issue_s=MDLabel(text='Date suppossed to return :', size_hint=(1,None),size=(1,20))
            self.date_issue_sr=MDLabel(text=self.date_supp, size_hint=(1,None),size=(1,20),halign='left')
            self.date_issue_r=MDLabel(text='Date book returned :', size_hint=(1,None),size=(1,20))
            self.date_issue_rr=MDLabel(text= self.date_ret, size_hint=(1,None),size=(1,20),halign='left')
            self.date_issue_p=MDLabel(text='Date passed by :', size_hint=(1,None),size=(1,20))
            self.date_issue_pr=MDLabel(text=self.date_pass, size_hint=(1,None),size=(1,20),halign='left')
            self.ids.gdl.add_widget(self.date_issue_l)
            self.ids.gdl.add_widget(self.date_issue_lr)
            self.ids.gdl.add_widget(self.date_issue_s)
            self.ids.gdl.add_widget(self.date_issue_sr)
            self.ids.gdl.add_widget(self.date_issue_r)
            self.ids.gdl.add_widget(self.date_issue_rr)
            self.ids.gdl.add_widget(self.date_issue_p)
            self.ids.gdl.add_widget(self.date_issue_pr)
            self.ids.showmore.text='Less'
            self.size=(1,190)
            self.ids.imgb.size=(80,80)
        else:
            self.ids.gdl.remove_widget(self.date_issue_l)
            self.ids.gdl.remove_widget(self.date_issue_lr)
            self.ids.gdl.remove_widget(self.date_issue_s)
            self.ids.gdl.remove_widget(self.date_issue_sr)
            self.ids.gdl.remove_widget(self.date_issue_r)
            self.ids.gdl.remove_widget(self.date_issue_rr)
            self.ids.gdl.remove_widget(self.date_issue_p)
            self.ids.gdl.remove_widget(self.date_issue_pr)
            self.ids.showmore.text='More...'
            self.size=(1,100)
            self.ids.imgb.size=(60,60)
            
#Image widget
class Imageframe(CardCommon):
    img=ObjectProperty()
    
    def __init__(self,source,**kwargs):
        super(Imageframe,self).__init__(**kwargs)
        self.ids.img.source=source

#Basic card changer
class CardChange(CardCommon):
    pass

#Card with a title and a separator that holds other widgets
class CardHolder(CardCommon):
    float1=ObjectProperty()
    lbltitle=ObjectProperty()
    sep=ObjectProperty()
    boxl=ObjectProperty()
    
    def __init__(self,**kwargs):
        super(CardHolder,self).__init__(**kwargs)

#A card that has a ScrollView
class ScrollWidget(CardCommon):
    grid=ObjectProperty()
    count=0
    def __init__(self,**kwargs):
        super(ScrollWidget,self).__init__(**kwargs) 

    def add_widgets(self,widget):
        self.ids.grid.add_widget(widget)
        
    def clear(self):
        self.ids.grid.clear_widgets()

#Navigator      
class Input(TextField):
    def __init__(self,**kwargs):
        self.next = kwargs.pop('next', None)
        super(Input,self).__init__(**kwargs)
        self.index=''
        
    def on_focus(self, instance, value):
        self.index=self
        
    def keyboard_on_key_down(self,window, keycode, text, modifiers):
        key, key_str = keycode
        if  key == 274 or key == 13:
            a=''
            b=[]
            item_no=0
            for chld in self.parent.children:
                
                a=str(chld)
                if a[:11]=='<__main__.I':
                    item_no+=1
                    b.append(chld)
            self.index_my=b.index(self.index)
            if self.index_my<=item_no:
                self.index_my-=1
                b[self.index_my].focus=True
                
        elif key==273:
            a=''
            b=[]
            item_no=0
            for chld in self.parent.children:
                a=str(chld)
                if a[:11]=='<__main__.I':
                    item_no+=1
                    b.append(chld)
            self.index_my=b.index(self.index)
        
            if self.index_my>=0 and self.index_my<(item_no)-1:
                self.index_my+=1
                b[self.index_my].focus=True
                    
        return TextField.keyboard_on_key_down(self, window, keycode, text, modifiers)    
    
    
class LableI(MDLabel):
    pass

class Label(MDLabel):
    pass

class Images_anim(Image):
    def __init__(self, **kwargs):
        super(Images_anim,self).__init__(**kwargs)

class Accordion_Buttons(Button):
    pass
class Header_left(Button):
    pass

class CustomDropdown(DropDown, HoverBehavior):
    elevation=NumericProperty(1)
    def on_enter(self):
        self.event=Clock.schedule_once(self.elevate_up,.6)     
    
    def elevate_up(self,*args):
        self.elevation= 4

    def on_leave(self):
        self.event.cancel()
        Clock.schedule_once(self.elevate_down,.6)
        
    def elevate_down(self,*args):
        self.elevation=1



#Navigator buttons
class MDiconB(HoverBehavior, IconButton):
    icon = StringProperty()
        
    def on_enter(self, *args):
        if self.icon ==u'\uF265':
            self.animation_enter('Clear form')
        elif self.icon ==u'\uF450':
            self.animation_enter('Update records from database')
        elif self.icon ==u'\uF4AB':
            self.animation_enter('Move to the first record')
        elif self.icon ==u'\uF4AE':
            self.animation_enter('Move to the previous record')
        elif self.icon ==u'\uF1BA':
            self.animation_enter('add records to database')
        elif self.icon ==u'\uF1C0':
            self.animation_enter('delete records from database')
        elif self.icon ==u'\uF4AD':
            self.animation_enter('Move to the next record')
        elif self.icon ==u'\uF4AC':
            self.animation_enter('Move to the last record')
        
    def on_leave(self, *args):
        self.animation_leave()

    def animation_enter(self,text):
        self.color = (1,1,1,1)
        try:
            self.parent.parent.parent.parent.parent.ids.float1.remove_widget(label)
        except:
            pass
        
        
        self.label=LableI(text=text,\
                     x=self.parent.parent.parent.parent.parent.ids.boxl.x,\
                        y=self.parent.parent.parent.parent.parent.ids.boxl.y-2)
        
        self.parent.parent.parent.parent.parent.ids.float1.add_widget(self.label)
        global anim
        anim=Animation(height=40,duration=.5,t='in_out_quart',\
                       y=self.parent.parent.parent.parent.parent.ids.boxl.y-40)
        anim.start(self.label)

    def animation_leave(self):
        self.color = (1,1,1,1)
        anim=Animation(height=10,duration=.1,t='in_out_quart',\
                       y=self.parent.parent.parent.parent.parent.ids.boxl.y-4)
        anim.start(self.label)
        anim.on_complete=self.parent.parent.parent.parent.parent.ids.float1.remove_widget


class Toolbar(ScrollView):
    clear_f=ObjectProperty()
    update=ObjectProperty()
    first_r=ObjectProperty()
    prev_r=ObjectProperty()
    add_r=ObjectProperty()
    del_r=ObjectProperty()
    next_r=ObjectProperty()
    last_r=ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Toolbar,self).__init__(**kwargs)

class Bg_p2d(BoxLayout):
    bg_color = ListProperty([0,0,0,0])

#Navigator card holder
class Navigator(CardHolder):
    img=Images_anim(pos_hint={'center_x':.5,'center_y':.5},size_hint=(None,None),size=(150,150), allow_stretch = True, keep_data = False)
    sm=ScreenManager()
    lbl_i=MDLabel(size=(200,100),size_hint=(None,None),pos_hint={'center_x':.5,'center_y':.2},markup=True) 
    
    def __init__(self,which_scroll='std_reg',**kwargs):
        super(Navigator,self).__init__(**kwargs)
        # set the title for the cardholder
        self.ids.lbltitle.text='Navigator'  
        
        #image results for successful addedd and deleted
        # screenmanager for changing the animation of results
        # results label for communication
        self.img=Images_anim(pos_hint={'center_x':.5,'center_y':.5},size_hint=(None,None),size=(150,150))
        self.sm=ScreenManager()
        self.lbl_i=MDLabel(size=(200,100),size_hint=(None,None),pos_hint={'center_x':.5,'center_y':.2},markup=True) 
    
        screen1=Screen(name='main') #screen for the details
        screen2=Screen(name='results') #screen for the results
        self.sm.add_widget(screen1)
        self.sm.add_widget(screen2)
        self.sm.transition=SwapTransition()

        #Choose which scroll_widget to put

        if which_scroll=='books_reg':
            self.scroll=Scrollwidget_Books()
        elif which_scroll=='books_reg_many':
            self.scroll=Scrollwidget_Books_many()
        elif which_scroll=='std_reg':
            self.scroll=Scrollwidget_std_reg()
        elif which_scroll=='teachers_reg':
            self.scroll=Scrollwidget_non_and_teacher_reg()
        elif which_scroll=='non_teaching_reg':
            self.scroll=Scrollwidget_non_and_teacher_reg()
        elif which_scroll=='std_issue':
            self.scroll=Scrollwidget_std_issue_return()
        elif which_scroll=='teachers_issue':
            self.scroll=Scrollwidget_non_teacher_issue_return()
        elif which_scroll=='non_teaching_issue':
            self.scroll=Scrollwidget_non_teacher_issue_return()
        
        screen1.add_widget(self.scroll)
        
        # Add the results image and label in the Screen2
        flt_anim=FloatLayout(size_hint=(1,1))
        flt_anim.add_widget(self.img)
        flt_anim.add_widget(self.lbl_i)
        screen2.add_widget(flt_anim)

        #From the boxlayout of the cardholder add the screenmanager and a toolbar
        self.tool=Toolbar()
        self.ids.boxl.add_widget(self.sm)
        self.ids.boxl.add_widget(self.tool)

    def show_add(self):
        self.sm.current='results'
        self.img.source='pic_control\\tick.png'
        self.lbl_i.text='Record added successfully'
        self.img.reload()
        Clock.schedule_once(self.return_screen,1)

    def show_delete(self):
        self.img.source='pic_control\\x.png'
        self.lbl_i.text='Record removed successfully'
        self.img.reload()
        self.sm.current='results'        
        Clock.schedule_once(self.return_screen,1)

    def return_screen(self,*args):
        self.sm.current='main'

    def get_nav_buttons(self):
        return self.tool.ids
    
    def get_scroll_input(self):
        Inputs=self.scroll.return_input()
        return Inputs

#Body for the navigator widget
#for books one reg
class Scrollwidget_Books(ScrollView):
    acc_n=ObjectProperty()
    isbn=ObjectProperty()
    tit=ObjectProperty()
    pubr=ObjectProperty()
    edition=ObjectProperty()
    auth=ObjectProperty()
    pob=ObjectProperty()
    yop=ObjectProperty()
    categ=ObjectProperty()
    shelve=ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Scrollwidget_Books,self).__init__(**kwargs)

    def return_input(self):
        return self.ids

#for books many reg
class Scrollwidget_Books_many(ScrollView):
    acc_n=ObjectProperty()
    isbn=ObjectProperty()
    tit=ObjectProperty()
    pubr=ObjectProperty()
    edition=ObjectProperty()
    auth=ObjectProperty()
    pob=ObjectProperty()
    yop=ObjectProperty()
    categ=ObjectProperty()
    shelve=ObjectProperty()
    book_q=ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Scrollwidget_Books_many,self).__init__(**kwargs)

    def return_input(self):
        return self.ids

#for student reg
class Scrollwidget_std_reg(ScrollView):
    adm_no=ObjectProperty()
    id_no=ObjectProperty()
    name=ObjectProperty()
    clas=ObjectProperty()
    gender_female=ObjectProperty()
    gender_male=ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Scrollwidget_std_reg,self).__init__(**kwargs)

    def return_input(self):
        return self.ids

#for Non-teaching stuff reg #for Techers reg
class Scrollwidget_non_and_teacher_reg(ScrollView):
    id_no=ObjectProperty()
    name=ObjectProperty()
    gender_female=ObjectProperty()
    gender_male=ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Scrollwidget_non_and_teacher_reg,self).__init__(**kwargs)

    def return_input(self):
        return self.ids


#for student issuing books
class Scrollwidget_std_issue_return(ScrollView):
    adm_no=ObjectProperty()
    id_no=ObjectProperty()
    name=ObjectProperty()
    clas=ObjectProperty()
    book_acc_no=ObjectProperty()
    titl=ObjectProperty()
    dat_issue=ObjectProperty()
    date_ret=ObjectProperty()
    pub=ObjectProperty()
    
    def __init__(self, **kwargs):
        super(Scrollwidget_std_issue_return, self).__init__(**kwargs)

    def return_input(self):
        return self.ids

#for teachers issuing books and on-teaching stuff issuing books and return
class Scrollwidget_non_teacher_issue_return(ScrollView):
    id_no=ObjectProperty()
    name=ObjectProperty()
    book_acc_no=ObjectProperty()
    titl=ObjectProperty()
    dat_issue=ObjectProperty()
    date_ret=ObjectProperty()
    pub=ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Scrollwidget_non_teacher_issue_return,self).__init__(**kwargs)

    def return_input(self):
        return self.ids
    

class Online_b(CardCommon):
    img=ObjectProperty()
    isbn=ObjectProperty()
    titl=ObjectProperty()
    auth=ObjectProperty()
    publ=ObjectProperty()
    yp=ObjectProperty()
    
    def __init__(self,img='',isbn='',titl='',auth='',publ='',year='',**kwargs):
        super(Online_b,self).__init__(**kwargs)
        self.ids.img.source=img
        self.ids.isbn.text=isbn
        self.ids.titl.text=titl
        self.ids.auth.text=auth
        self.ids.publ.text=publ
        self.ids.yp.text=year

class Updatedialog(CardCommon):
    pass

class Deletedialog(CardCommon):
    pass
    
#main screen manager
class ScreenM(ScreenManager):
    try:
        # tries to connect if returns an error the database doent exists else it exits
        connection = sqlite3.connect('file:database.db?mode=rw', uri=True)
        cursor=connection.cursor()
    except sqlite3.OperationalError:
        # if the db doent exists then create a new database with relevant tables
        connection = sqlite3.connect('file:database.db?mode=rwc', uri=True)
        cursor=connection.cursor()

        #create tables for books
        cursor.execute(''' CREATE TABLE books(
                            book_accession_no INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER ,
                            isbn TEXT,
                            title TEXT,
                            publisher TEXT,
                            edition TEXT,
                            author TEXT,
                            place_of_publication TEXT,
                            year_of_publication TEXT,
                            category  TEXT,
                            shelve_no  TEXT,
                            lost  TEXT,
                            lost_by TEXT,
                            borrowed  TEXT,
                            borrowed_by TEXT,
                            damaged TEXT,
                            damaged_by TEXT,
                            by_user TEXT )  ''')

        #create table for members
        cursor.execute(''' CREATE TABLE members(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        adm_no TEXT,
                        class  TEXT,
                        id_no TEXT,
                        name TEXT,
                        gender TEXT,
                        remarks TEXT,
                        deactivate TEXT,
                        date_deactivate  TEXT,
                        date_to_active  TEXT,
                        member_type  TEXT,
                        by_user TEXT) ''')
        
        #create table for borrow
        cursor.execute(''' CREATE TABLE borrow(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        adm_no  TEXT,
                        id_no  TEXT,
                        date_issued  TEXT,
                        date_suppossed_return TEXT,
                        date_returned  TEXT,
                        date_passed_by  TEXT,
                        book_accession_no  TEXT,
                        member_type  TEXT,
                        by_user TEXT) ''')
        
        #create table for history
        cursor.execute(''' CREATE TABLE history(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        book_accession_no  TEXT,
                        adm_no  TEXT,
                        id_no  TEXT,
                        date_issued  TEXT,
                        date_suppossed_return TEXT,
                        date_returned  TEXT,
                        date_passed_by  TEXT,
                        by_user TEXT) ''')

    #Reference for widgets
    stack_dash=ObjectProperty()
    sm_content=ObjectProperty()
    stack_book_reg=ObjectProperty()
    stack_student_reg=ObjectProperty()
    stack_teachers_reg=ObjectProperty()
    stack_non_teaching_reg=ObjectProperty()
    stack_admin_center=ObjectProperty()
    stack_notifications=ObjectProperty()
    stack_settings=ObjectProperty()
    stack_backup_center=ObjectProperty()
    stack_analysis=ObjectProperty()
    stack_non_teaching_borro_ret=ObjectProperty()
    stack_Teachers_borro_ret=ObjectProperty()
    stack_Students_borro_ret=ObjectProperty()
    stack_book_reg_many=ObjectProperty()
    stack_book_reg_table=ObjectProperty()
    box_notify=ObjectProperty()
    previous_date=ObjectProperty()
    backup_grd=ObjectProperty()
    rvanlysis=ObjectProperty()
    lbl_title0=ObjectProperty()
    graph_plot0=ObjectProperty()
    lbl_analysis0=ObjectProperty()
    lbl_title1=ObjectProperty()
    graph_plot1=ObjectProperty()
    lbl_analysis1=ObjectProperty()
    books_search=ObjectProperty()
    mdicon_table=ObjectProperty()
    txtpasswd=ObjectProperty()
    prof_pic=StringProperty('pic_control\\icon.ico')
    barcode_preview=ObjectProperty()
    img_preview=ObjectProperty()
    lbl_preview=ObjectProperty()
    margin_x=ObjectProperty()
    margin_y=ObjectProperty()
    nocpp=ObjectProperty()
    norpp=ObjectProperty()
    sbbx=ObjectProperty()
    sbby=ObjectProperty()
    chkbx_lost=ObjectProperty()
    chkbx_damaged=ObjectProperty()
    chkbx_return=ObjectProperty()
    rv_ret=ObjectProperty()
    rv_issue=ObjectProperty()
    apply_b_i=ObjectProperty()
    header_wall = StringProperty('')
    rst_records = ListProperty()
    line_nav = BooleanProperty(False)
    giff_image = ObjectProperty(Image(source='pics\\leaf.zip', mipmap=True,\
                                      anim_delay=0.1))
    autocomplete = False
    
    #global variables
    user_name='Administrator'
    existing=[]
    for filename in glob.iglob('*.txt'):
         existing.append(filename)

    #books registration database counter
    if 'index_books_reg.txt' not in existing:
        file=open('index_books_reg.txt','w')
        file.write('0')
        index_books_reg=0
    elif 'index_books_reg.txt' in existing:
        file=open('index_books_reg.txt','r')
        index_books_reg=int(file.read())
    file.close()
    
    #students registration database counter
    if 'index_std_reg.txt' not in existing:
        file=open('index_std_reg.txt','w')
        file.write('0')
        index_std_reg=0
    elif 'index_std_reg.txt' in existing:
        file=open('index_std_reg.txt','r')
        index_std_reg=int(file.read())
    file.close()

    #teachers registration database counter
    if 'index_teach_reg.txt' not in existing:
        file=open('index_teach_reg.txt','w')
        file.write('0')
        index_teach_reg=0
    elif 'index_teach_reg.txt' in existing:
        file=open('index_teach_reg.txt','r')
        index_teach_reg=int(file.read())
    file.close()

    #non teaching registration database counter
    if 'index_non_reg.txt' not in existing:
        file=open('index_non_reg.txt','w')
        file.write('0')
        index_non_reg=0
    elif 'index_non_reg.txt' in existing:
        file=open('index_non_reg.txt','r')
        index_non_reg=int(file.read())
    file.close()

    #students circulation database counter
    if 'index_std_circ.txt' not in existing:
        file=open('index_std_circ.txt','w')
        file.write('0')
        index_std_circ=0
    elif 'index_std_circ.txt' in existing:
        file=open('index_std_circ.txt','r')
        index_std_circ=int(file.read())
    file.close()

    #teachers circulation database counter
    if 'index_teach_circ.txt' not in existing:
        file=open('index_teach_circ.txt','w')
        file.write('0')
        index_teach_circ=0
    elif 'index_teach_circ.txt' in existing:
        file=open('index_teach_circ.txt','r')
        index_teach_circ=int(file.read())
    file.close()

    #non teaching circulation database counter
    if 'index_non_circ.txt' not in existing:
        file=open('index_non_circ.txt','w')
        file.write('0')
        index_non_circ=0
    elif 'index_non_circ.txt' in existing:
        file=open('index_non_circ.txt','r')
        index_non_circ=int(file.read())
    file.close()

    #backup counter
    if 'backup_counter.txt' not in existing:
        file=open('backup_counter.txt','w')
        file.write('0')
        backup_counter=0
    elif 'backup_counter.txt' in existing:
        file=open('backup_counter.txt','r')
        backup_counter=int(file.read())
    file.close()

    #backup counter
    if 'page_settings.txt' not in existing:
        file=open('page_settings.txt','w')
        page_settings={'cols':4, 'rows':8, 'margin_x':10, 'margin_y':50, 'space_x':120, 'space_y':100}
        file.write(str(page_settings))
    elif 'page_settings.txt' in existing:
        file=open('page_settings.txt','r')
        page_settings=ast.literal_eval(file.read())
        
    file.close()

    #times to borrow
    if 'times_borrowed.txt' not in existing:
        file=open('times_borrowed.txt','w')
        file.write('[6,6,6]')
        times_borrowed=[6,6,6]
    elif 'times_borrowed.txt' in existing:
        file=open('times_borrowed.txt','r')
        times_borrowed=ast.literal_eval(file.read())
    file.close()
    
    #check if backup path exists if not create the path
    if os.path.isdir("backups")==False:
        os.mkdir('backups')
    
    #checks whether there is folders for students teachers and non teaching stuff and profile pic exists

    files=[]
    for (dirpath, dirnames, filenames) in os.walk('.'):
        files.extend(dirnames)
        break
    
    if 'std_pic' not in files:
        os.mkdir('std_pic')
    if 'teach_pic' not in files:
        os.mkdir('teach_pic')
    if 'non_pics' not in files:
        os.mkdir('non_pics')
    if 'barcode_file' not in files:
        os.mkdir('barcode_file')
    if 'reports' not in files:
        os.mkdir('reports')
        
    filesz=[]
    for (dirpath, dirnames, filenames) in os.walk('barcode_file'):
        filesz.extend(dirnames)
        break
    if 'barcode_images' not in filesz:
        os.mkdir('barcode_file\\barcode_images\\')

    filez=[]
    for (dirpath, dirnames, filenames) in os.walk('reports'):
        filez.extend(dirnames)
        break
    if 'reports_images' not in filez:
        os.mkdir('reports\\reports_images')
    
    
    #check the availablity of the images and stores them in a variable
    std_pics=[]
    for (dirpath, dirnames, filenames) in os.walk('std_pic\\'):
        std_pics.extend(filenames)
        break

    teach_pics=[]
    for (dirpath, dirnames, filenames) in os.walk('teach_pic\\'):
        teach_pics.extend(filenames)
        break

    non_pics=[]
    for (dirpath, dirnames, filenames) in os.walk('non_pics\\'):
        non_pics.extend(filenames)
        break

    if 'profile_pic' not in files:
        os.mkdir('profile_pic')
        
    
    def __init__(self,**kwargs):
        super(ScreenM,self).__init__(**kwargs)
        #putting drop down to search
        searches = ['Search by Book title',\
                    'Search by Publisher',\
                    'Search by Author',\
                    'Search by Place of publication',\
                    'Search by Year of publication',\
                    'Search by category',\
                    'Search by book accession no.',\
                    'Search by shelve no.',\
                    'Search by lost book',\
                    'Search by borrowed book',\
                    'Search by damaged book',\
                    'Search by Admission no',\
                    'Search by class'
                    ]
        self.dropdown = CustomDropdown()
        self.dropdown.dismiss_on_select=False
        self.criteria = 'Search by Book title'

        self.ids.txt_b_std.text= str(self.times_borrowed[0])
        self.ids.txt_b_tch.text=str(self.times_borrowed[1])
        self.ids.txt_b_nontch.text=str(self.times_borrowed[2])
        
        for criteria in searches:
            if criteria=='Search by Book title':
                lbl = MDLabel(text = 'Criteria for books',font_style='Subhead',size_hint_y=None, height=20 )
                self.dropdown.add_widget(lbl)
                bb = CustomTgglButton(text=criteria, size_hint_y=None, height=20,group = 'a', state = 'down')
            elif  criteria=='Search by class':
                lbl = MDLabel(text = 'Criteria for borrowers',font_style='Subhead',size_hint_y=None, height=20 )
                self.dropdown.add_widget(lbl)
                bb = CustomTgglButton(text=criteria, size_hint_y=None, height=20, group = 'b')
            else:
                bb = CustomTgglButton(text=criteria, size_hint_y=None, height=20,group = 'a' )
                
            bb.bind(on_release=self.specify_citeria)
            self.dropdown.add_widget(bb)

        
        self.ids.attch_btn.bind(on_release=self.dropdown.open)
        
        self.ids.online_t.ids.txt.bind(on_text_validate=partial(self.load_internet_controls, self.ids.online_t.ids.txt.text))
        

        self.transition=SwapTransition()

        self.ids.sm_content.transition = CardTransition()
        self.ids.sm_content.transition.direction='up'
        self.ids.sm_content.transition.mode='push'
        
        self.ids.sm_content.current='dashboard'
        self.ids.sm_title.transition.direction='up'
        self.ids.sm_title.transition.mode='push'

        existing=[]
        for filename in glob.iglob('*.dat'):
             existing.append(filename)

        #books registration database counter
        if 'pky.dat' not in existing:
            self.current = 'Registration'
        elif 'pky.dat' in existing:
            self.current = 'login'
        
    
        #card changer for notifications and total number of books
##        cardchanger0=CardChange(size_hint=(.38,.4)) # total books items cardchanger
##        cardchanger1=CardChange(size_hint=(.38,.4)) # Recent places cardholder
##        self.screenMn=ScreenMN(size_hint=(1,1))
##        self.screenMn.transition=CardTransition()
##        self.screenMn.transition.direction= 'up'
##        self.screenMn.transition.mode='push'
##        cardchanger0.add_widget(self.screenMn)
##
##        #add the total number of books
##        self.dashlabel=DashLabel()
##        cardchanger1.add_widget( self.dashlabel)
##        
##        #self.ids.stack_dash.add_widget(cardchanger0)
##        #self.ids.stack_dash.add_widget(cardchanger1)
        
        ########## REGISTRATION WIDGETS ############
        #screenmanager for one & mass book registration
        self.screen_book_reg=Carousel(size_hint=(.5,1), anim_type='out_expo')
        self.screen_book_reg.bind(index=partial(self.change_crr,self.screen_book_reg))
        self.screen_book_reg.transition=CardTransition()
        self.screen_book_reg.transition.direction='left'
        self.screen_one_reg=Screen(name='one')
        self.screen_many_reg=Screen(name='mass')
        flt_one_reg=BoxLayout(padding=(0,0,0,40))
        flt_many_reg=BoxLayout(padding=(0,0,0,40))
        
        self.screen_book_reg.add_widget(self.screen_one_reg)
        self.screen_book_reg.add_widget(self.screen_many_reg)
        
        #add widgets for one book registration
        self.nav_books= Navigator(which_scroll='books_reg',size_hint=(1,1))
        flt_one_reg.add_widget(self.nav_books)
        self.screen_one_reg.add_widget(flt_one_reg) # add navigator to screen one reg
        self.nav_books.ids.lbltitle.text='One book registration form'
        self.inputs= self.nav_books.get_scroll_input()
        self.cardholder_bk_reg= CardHolder(size_hint=(.48,1))
        self.cardholder_bk_reg.ids.lbltitle.text='Online Search results'
        self.ids.stack_book_reg.add_widget(self.cardholder_bk_reg)
        cd = CardCommon(size_hint=(.5,1))
        cd.add_widget(self.screen_book_reg)
        self.ids.stack_book_reg.add_widget(cd)

        #Bind controls for one book registration
        #get the scroll contents and buttons
        self.one_book_scroll_inputs=self.nav_books.get_scroll_input()
        self.one_book_nav_buttons=self.nav_books.get_nav_buttons()
        
        #move to record
        #refresh 
        self.one_book_nav_buttons['clear_f'].bind(on_press=partial(self.clear_content_for_scroll,self.one_book_scroll_inputs))
        #Update
        self.one_book_nav_buttons['update'].bind(on_press=self.update_once_one_book)
        #first
        self.one_book_nav_buttons['first_r'].bind(on_press=partial(self.move_to_first_record_books,self.one_book_scroll_inputs,self.nav_books))
        #previous
        self.one_book_nav_buttons['prev_r'].bind(on_press=partial(self.move_to_prev_record_books,self.one_book_scroll_inputs,self.nav_books))
        #add record
        self.one_book_nav_buttons['add_r'].bind(on_press=self.add_one_book_record)
        #delete
        self.one_book_nav_buttons['del_r'].bind(on_press=partial(self.delete_one_book,self.nav_books,self.one_book_scroll_inputs, 'No'))
        #next
        self.one_book_nav_buttons['next_r'].bind(on_press=partial(self.move_to_next_record_books,self.one_book_scroll_inputs,self.nav_books))
        #last
        self.one_book_nav_buttons['last_r'].bind(on_press=partial(self.move_to_last_record_books,self.one_book_scroll_inputs,self.nav_books))

        #bind search keytext
        self.one_book_scroll_inputs['acc_n'].bind(on_text_validate=self.display_results_one_book)

        #bind title search keytext
        self.one_book_scroll_inputs['tit'].bind(text=partial(self.auto_complete_feature, self.one_book_scroll_inputs))
        
        
        #add widgets for many books registration
        self.nav_books_many= Navigator(which_scroll='books_reg_many',size_hint=(1,1))
        flt_many_reg.add_widget(self.nav_books_many)
        self.screen_many_reg.add_widget(flt_many_reg) # add navigator to screen one reg
        self.nav_books_many.ids.lbltitle.text='Mass book registration form'
        
        #Bind controls for many book registration
        #get the scroll contents and buttons
        self.many_book_scroll_inputs=self.nav_books_many.get_scroll_input()
        self.many_book_nav_buttons=self.nav_books_many.get_nav_buttons()

        #move to record
        #clear
        self.many_book_nav_buttons['clear_f'].bind(on_press=partial(self.clear_content_for_scroll,self.many_book_scroll_inputs))
        #Update
        self.many_book_nav_buttons['update'].bind(on_press=partial(self.show_update_range_popup))
        #first
        self.many_book_nav_buttons['first_r'].bind(on_press=partial(self.move_to_first_record_books,self.many_book_scroll_inputs,self.nav_books_many))
        #previous
        self.many_book_nav_buttons['prev_r'].bind(on_press=partial(self.move_to_prev_record_books,self.many_book_scroll_inputs,self.nav_books_many))
        #add record
        self.many_book_nav_buttons['add_r'].bind(on_press=self.add_many_book_record)
        #Delete
        self.many_book_nav_buttons['del_r'].bind(on_press=partial(self.show_delete_range_popup,self.nav_books_many,self.many_book_scroll_inputs))
        
        #next
        self.many_book_nav_buttons['next_r'].bind(on_press=partial(self.move_to_next_record_books,self.many_book_scroll_inputs,self.nav_books_many))
        #last
        self.many_book_nav_buttons['last_r'].bind(on_press=partial(self.move_to_last_record_books,self.many_book_scroll_inputs,self.nav_books_many))

        #bind search keytext
        self.many_book_scroll_inputs['acc_n'].bind(on_text_validate=self.display_results_many_book)
        #bind title search keytext
        self.many_book_scroll_inputs['tit'].bind(text=partial(self.auto_complete_feature, self.many_book_scroll_inputs))
        

        #Table for books database
        self.table_books=TableWidget()
        self.stack_book_reg_table.add_widget(self.table_books)
        
        ############################################ Member Registration
        #add widgets for students registration
        self.img_std= Imageframe(source='pics\\account.png',size_hint=(.4,.6))
        self.navigator_std= Navigator(which_scroll='std_reg',size_hint=(.6,.95))
        self.navigator_std.ids.lbltitle.text='Students registration form'
        self.ids.stack_student_reg.add_widget(self.img_std)
        self.ids.stack_student_reg.add_widget(self.navigator_std)

        #put widgets to variable
        self.wid_mem_std_scrolls=self.navigator_std.get_scroll_input()
        self.wid_mem_std_input=self.navigator_std.get_nav_buttons()

        #clear
        self.wid_mem_std_input['clear_f'].bind(on_press=partial(self.clear_std_controls,self.wid_mem_std_scrolls))
        #Update
        self.wid_mem_std_input['update'].bind(on_press=self.update_std_reg)
        #first
        self.wid_mem_std_input['first_r'].bind(on_press=partial(self.move_to_first_record_std,self.wid_mem_std_scrolls,self.navigator_std))        
        #previous
        self.wid_mem_std_input['prev_r'].bind(on_press=partial(self.move_to_prev_record_std,self.wid_mem_std_scrolls,self.navigator_std))
        #add record
        self.wid_mem_std_input['add_r'].bind(on_press=self.add_member_std)
        #Delete
        self.wid_mem_std_input['del_r'].bind(on_press=self.delete_std)
        #next
        self.wid_mem_std_input['next_r'].bind(on_press=partial(self.move_to_next_record_std, self.wid_mem_std_scrolls, self.navigator_std))
        #last
        self.wid_mem_std_input['last_r'].bind(on_press=partial(self.move_to_last_record_std,self.wid_mem_std_scrolls,self.navigator_std))
        
        #bind search keytext for std
        self.wid_mem_std_scrolls['adm_no'].bind(on_text_validate=self.display_results_std_book)

        
        #add widgets for teachers registration
        self.img_teachers= Imageframe(source='pics\\account.png',size_hint=(.38,.6))
        self.navigator_teachers= Navigator(which_scroll='teachers_reg',size_hint=(.6,.95))
        self.navigator_teachers.ids.lbltitle.text='Teacher registration form'
        self.ids.stack_teachers_reg.add_widget(self.img_teachers)
        self.ids.stack_teachers_reg.add_widget(self.navigator_teachers)

        #get scroll and inputs
        self.wid_mem_teachers_scrolls=self.navigator_teachers.get_scroll_input()
        self.wid_mem_teachers_input=self.navigator_teachers.get_nav_buttons()

        #clear
        self.wid_mem_teachers_input['clear_f'].bind(on_press=partial(self.clear_tan_controls,self.wid_mem_teachers_scrolls))
        #Update
        self.wid_mem_teachers_input['update'].bind(on_press=partial(self.update_tan_reg,self.wid_mem_teachers_scrolls,\
                                                                    self.navigator_teachers))
        #first
        self.wid_mem_teachers_input['first_r'].bind(on_press=partial(self.move_to_first_record_tan,self.wid_mem_teachers_scrolls,\
                                                                     self.navigator_teachers,self.index_teach_reg,'index_teach_reg','t'))        
        #previous
        self.wid_mem_teachers_input['prev_r'].bind(on_press=partial(self.move_to_prev_record_tan,self.wid_mem_teachers_scrolls,\
                                                                     self.navigator_teachers,self.index_teach_reg,'t'))
        #add record
        self.wid_mem_teachers_input['add_r'].bind(on_press=partial(self.add_member_tan,self.wid_mem_teachers_scrolls,\
                                                                   self.navigator_teachers,self.wid_mem_teachers_input,'t'))
        #Delete
        self.wid_mem_teachers_input['del_r'].bind(on_press=partial(self.delete_tan,self.navigator_teachers,self.wid_mem_teachers_scrolls))
        #next
        self.wid_mem_teachers_input['next_r'].bind(on_press=partial(self.move_to_next_record_tan,self.wid_mem_teachers_scrolls,\
                                                                     self.navigator_teachers,self.index_teach_reg,'t'))
        #last
        self.wid_mem_teachers_input['last_r'].bind(on_press=partial(self.move_to_last_record_tan,self.wid_mem_teachers_scrolls,\
                                                                     self.navigator_teachers,self.index_teach_reg,'index_teach_reg','t'))

        #bind search keytext for teachers
        self.wid_mem_teachers_scrolls['id_no'].bind(on_text_validate=self.display_results_teach_book)

        #add widgets for non-teachers registration
        self.img_non_teaching= Imageframe(source='pics\\account.png',size_hint=(.38,.6))
        self.navigator_non_teaching= Navigator(which_scroll='non_teaching_reg',size_hint=(.6,.95))
        self.navigator_non_teaching.ids.lbltitle.text='Non teaching stuff registration form'
        self.ids.stack_non_teaching_reg.add_widget(self.img_non_teaching)
        self.ids.stack_non_teaching_reg.add_widget(self.navigator_non_teaching)

        #get scroll and inputs
        self.wid_mem_non_scrolls=self.navigator_non_teaching.get_scroll_input()
        self.wid_mem_non_input=self.navigator_non_teaching.get_nav_buttons()
        #clear
        self.wid_mem_non_input['clear_f'].bind(on_press=partial(self.clear_tan_controls,self.wid_mem_non_scrolls))
        #Update
        self.wid_mem_non_input['update'].bind(on_press=partial(self.update_tan_reg,self.wid_mem_non_scrolls,\
                                                                    self.navigator_non_teaching))
        #first
        self.wid_mem_non_input['first_r'].bind(on_press=partial(self.move_to_first_record_tan,self.wid_mem_non_scrolls,\
                                                                     self.navigator_non_teaching,self.index_non_reg,'index_non_reg','n'))        
        #previous
        self.wid_mem_non_input['prev_r'].bind(on_press=partial(self.move_to_prev_record_tan,self.wid_mem_non_scrolls,\
                                                                     self.navigator_non_teaching,self.index_non_reg,'n'))
        #add record
        self.wid_mem_non_input['add_r'].bind(on_press=partial(self.add_member_tan,self.wid_mem_non_scrolls,\
                                                                   self.navigator_non_teaching,self.wid_mem_non_input,'n'))
        #Delete
        self.wid_mem_non_input['del_r'].bind(on_press=partial(self.delete_tan,self.navigator_non_teaching,self.wid_mem_non_scrolls))
        #next
        self.wid_mem_non_input['next_r'].bind(on_press=partial(self.move_to_next_record_tan,self.wid_mem_non_scrolls,\
                                                                     self.navigator_non_teaching,self.index_non_reg,'n'))
        #last
        self.wid_mem_non_input['last_r'].bind(on_press=partial(self.move_to_last_record_tan,self.wid_mem_non_scrolls,\
                                                                     self.navigator_non_teaching,self.index_non_reg,'index_non_reg','n'))

        #bind search keytext for non teachers
        self.wid_mem_non_scrolls['id_no'].bind(on_text_validate=self.display_results_non_book)

        ############# BOOKS CIRCULATION ##############
        
        #add widgets for students issue and return
        self.img_std_issue=Imageframe(source='pics\\account.png',size_hint=(1,.6))
        self.nav_std_issue=Navigator(which_scroll='std_issue')
        self.actd_std=IconButton\
                       (text =u'\uF33E',font_size='24sp',size=(48,48),color=(0,0,0,.63),pos_hint={'right':.97,'center_y':.5})
        self.actd_std0=IconButton\
                        (text =u'\uF33F',font_size='24sp',x=self.actd_std.x,\
                                size=(48,48),color=(0,0,0,.63),pos_hint={'right':.9,'center_y':.5})
        self.nav_std_issue.ids.float1.add_widget(self.actd_std)
        self.nav_std_issue.ids.float1.add_widget(self.actd_std0)
        
        self.nav_std_issue.ids.lbltitle.text='Students book circulation form'
        self.current_std_issue=CardHolder(size_hint=(1, .91))
        self.current_std_issue.ids.lbltitle.text='Current borrowed books'
        #add scroll to borrow
        scroll_widget_std_issue=ScrollView(size_hint=(1,1))
        self.current_std_issue.ids.boxl.add_widget(scroll_widget_std_issue)
        self.Gridlayout_std_issue=GridLayout(cols=1,spacing=20,size_hint_y=None,padding=(5,5,5,10))
        self.Gridlayout_std_issue.bind(minimum_height=self.Gridlayout_std_issue.setter('height'))
        scroll_widget_std_issue.add_widget(self.Gridlayout_std_issue)
        
        self.history_std_issue=CardHolder(size_hint=(1, .91))
        self.history_std_issue.ids.lbltitle.text='History of books'
        #self.ref_history_std=Button(background_normal ='refresh',pos_hint={'center_x':.9,'center_y':.5},theme_text_color='Custom',text_color=(0,0,0,.5))
        #self.history_std_issue.ids.float1.add_widget(self.ref_history_std)
        #self.ref_history_std.bind(on_press=partial(self.show_history_books,'s'))
        #add scroll for history
        scroll_widget_std_history=ScrollView(size_hint=(1,1))
        self.history_std_issue.ids.boxl.add_widget(scroll_widget_std_history)
        self.Gridlayout_std_history=GridLayout(cols=1,spacing=10,size_hint_y=None,padding=(5,5,5,5))
        self.Gridlayout_std_history.bind(minimum_height=self.Gridlayout_std_history.setter('height'))
        scroll_widget_std_history.add_widget(self.Gridlayout_std_history)
        
        self.remark_std_issue=CardHolder(size_hint=(1,.33))
        self.remark_std_issue.ids.lbltitle.text='Remarks'
        self.txt_remarks=TextInput(multiline=True,size_hint=(1,1),hint_text='Type remarks here', background_color = (1,1,1,0),\
                                   background_normal = '', background_active = '', cursor_color = (0/255, 109/255, 240/255, 1),hint_text_color=(0,0,0,.8))
        
        self.remark_std_issue.ids.boxl.add_widget(self.txt_remarks)
        self.remark_std_issue.ids.boxl.padding=(20,0,20,0)
        self.ref_remarks_std=IconButton(text =u'\uF450',font_size='24sp', size=(48,48),pos_hint={'center_x':.9,'center_y':.5},theme_text_color='Custom',text_color=(0,0,0,.5))
        self.remark_std_issue.ids.float1.add_widget(self.ref_remarks_std)

        #search tab borrow
        self.searchtab_std_borrow=Search_Tab(size_hint=(1,.09),size=(600,60), pos_hint={'center_x':.5,'center_y':1})
        #search tab history
        self.searchtab_std_history=Search_Tab(size_hint=(1,.09),size=(600,60), pos_hint={'center_x':.5,'center_y':1})

        
        self.boxl_std0 = BoxLayout(padding = (20,20,20,20), spacing = 20)
        self.boxl_std1 = BoxLayout(spacing = 20, orientation = 'vertical', size_hint_x = .4)
        self.boxl_std2 = BoxLayout(size_hint_x = .6, padding = (0,0,0,40))
        self.boxl_std1.add_widget(self.img_std_issue)
        self.boxl_std1.add_widget(self.remark_std_issue)
        self.boxl_std2.add_widget(self.nav_std_issue)
        self.boxl_std0.add_widget(self.boxl_std1)
        self.boxl_std0.add_widget(self.boxl_std2)
        self.boxl_std3 = BoxLayout(size_hint_y=None,height=dp(600),padding = (20,20,20,20), spacing = 20, orientation='vertical')
        self.boxl_std4 = BoxLayout(size_hint_y=None,height=dp(600),padding = (20,20,20,20), spacing = 20, orientation='vertical')
        self.boxl_std3.add_widget(self.searchtab_std_borrow)
        self.boxl_std3.add_widget(self.current_std_issue)
        self.boxl_std4.add_widget(self.searchtab_std_history)
        self.boxl_std4.add_widget(self.history_std_issue)

        #nav
        scrll_nav0 = ScrollView(scroll_type=['bars'], bar_width = dp(15),bar_color=( 0, 52/255, 102/255, 1))
        box_nav0 =BoxWhite(size_hint_y=None, orientation='vertical')
        box_nav0.bind(minimum_height=box_nav0.setter('height'))
        scrll_nav0.add_widget(box_nav0)
        
        box_nav0.add_widget(self.boxl_std3)
        box_nav0.add_widget(self.boxl_std4)

        self.ids.stack_Students_borro_ret.add_widget(scrll_nav0)
        self.ids.stack_Students_borro_ret.add_widget(self.boxl_std0)
        
        
        #get scroll and inputs
        self.wid_std_circ_scrolls=self.nav_std_issue.get_scroll_input()
        self.wid_std_circ_input=self.nav_std_issue.get_nav_buttons()

        self.wid_std_circ_scrolls['adm_no'].bind(on_text_validate=partial(self.std_search_circ_for_std,self.txt_remarks)) 
        self.wid_std_circ_scrolls['book_acc_no'].bind(on_text_validate=self.book_search_circ_for_std)
        
        #search for history
        self.searchtab_std_history.ids.btn.bind(on_press=partial(self.do_search_for_records_circ, self.wid_std_circ_scrolls, self.searchtab_std_history.ids.txt, \
                                                                 None, self.Gridlayout_std_history,'s','hst'))
        self.searchtab_std_history.ids.txt.bind(on_text_validate=partial(self.do_search_for_records_circ, self.wid_std_circ_scrolls, self.searchtab_std_history.ids.txt, \
                                                               None, self.Gridlayout_std_history,'s','hst'))
        
        #search for borrow
        self.searchtab_std_borrow.ids.btn.bind(on_press=partial(self.do_search_for_records_circ, self.wid_std_circ_scrolls, self.searchtab_std_borrow.ids.txt, \
                                                                 self.Gridlayout_std_issue, None,'s','br'))
        self.searchtab_std_borrow.ids.txt.bind(on_text_validate=partial(self.do_search_for_records_circ, self.wid_std_circ_scrolls, self.searchtab_std_borrow.ids.txt, \
                                                               self.Gridlayout_std_issue, None,'s','br'))

        #show menu act/deact
        self.actd_std.bind(on_release=partial(self.to_deactivate_member,self.wid_std_circ_scrolls, 's','deactivate'))
        self.actd_std0.bind(on_release=partial(self.to_deactivate_member,self.wid_std_circ_scrolls, 's','activate'))
        
         #refresh remarks
        self.ref_remarks_std.bind(on_press=partial(self.update_remarks,self.wid_std_circ_scrolls,'s'))
        #clear
        self.wid_std_circ_input['clear_f'].bind(on_press=partial(self.clear_form_circ,self.wid_std_circ_scrolls,'s' ))                                                 
        #update
        self.wid_std_circ_input['update'].bind(on_press=partial(self.update_record_circ,self.wid_std_circ_scrolls ))                                                 
        #first
        self.wid_std_circ_input['first_r'].bind(on_press=partial(self.move_to_first_record_circ,self.wid_std_circ_scrolls,\
                                                                     self.nav_std_issue,'s'))
        #previous
        self.wid_std_circ_input['prev_r'].bind(on_press=partial(self.move_to_prev_record_circ,self.wid_std_circ_scrolls,\
                                                                     self.nav_std_issue,'s'))
        #add record
        self.wid_std_circ_input['add_r'].bind(on_press=partial(self.combined_circ_add_rec, self.wid_std_circ_scrolls, self.nav_std_issue,\
                                                               self.wid_std_circ_input,'s'))
        #next
        self.wid_std_circ_input['next_r'].bind(on_press=partial(self.move_to_next_record_circ,self.wid_std_circ_scrolls,\
                                                                     self.nav_std_issue,'s'))
        #last
        self.wid_std_circ_input['last_r'].bind(on_press=partial(self.move_to_last_record_circ,self.wid_std_circ_scrolls,\
                                                                     self.nav_std_issue,'s'))
        
        self.wid_std_circ_input['del_r'].disabled=True                                                            
                                      
        #add widgets for teachers issue and return
        self.img_teachers_issue=Imageframe(source='pics\\account.png',size_hint=(1,.6))
        self.nav_teachers_issue=Navigator(which_scroll='teachers_issue')
        self.actd_teach0=IconButton(text =u'\uF33F',font_size='24sp',\
                                size=(48,48),color=(0,0,0,.63),pos_hint={'right':.9,'center_y':.5})
        self.nav_teachers_issue.ids.float1.add_widget(self.actd_teach0)
        self.actd_teach=IconButton(text =u'\uF33E',font_size='24sp',\
                                size=(48,48),color=(0,0,0,.63),pos_hint={'right':.97,'center_y':.5})
        self.nav_teachers_issue.ids.float1.add_widget(self.actd_teach)
        
        self.nav_teachers_issue.ids.lbltitle.text='Teachers book circulation form'
        self.current_Teachers_issue=CardHolder(size_hint=(1,.91))
        self.current_Teachers_issue.ids.lbltitle.text='Current borrowed books'
        #add scroll to teacher borrow
        scroll_widget_teach_issue=ScrollView(size_hint=(1,1),scroll_type=['bars'])
        self.current_Teachers_issue.ids.boxl.add_widget(scroll_widget_teach_issue)
        self.Gridlayout_teach_issue=GridLayout(cols=1,spacing=20,size_hint_y=None,padding=(5,5,5,10))
        self.Gridlayout_teach_issue.bind(minimum_height=self.Gridlayout_teach_issue.setter('height'))
        scroll_widget_teach_issue.add_widget(self.Gridlayout_teach_issue)
        
        self.history_teach_issue=CardHolder(size_hint=(1,.91))
        self.history_teach_issue.ids.lbltitle.text='History of books'
        #self.ref_history_teach=Button(background_normal ='refresh',pos_hint={'center_x':.9,'center_y':.5},theme_text_color='Custom',text_color=(0,0,0,.5))
        #self.history_teach_issue.ids.float1.add_widget(self.ref_history_teach)
       # self.ref_history_teach.bind(on_press=partial(self.show_history_books,'t'))
        
        #add scroll for history
        scroll_widget_teach_history=ScrollView(size_hint=(1,1))
        self.history_teach_issue.ids.boxl.add_widget(scroll_widget_teach_history)
        self.Gridlayout_teach_history=GridLayout(cols=1,spacing=10,size_hint_y=None,padding=(5,5,5,5))
        self.Gridlayout_teach_history.bind(minimum_height=self.Gridlayout_teach_history.setter('height'))
        scroll_widget_teach_history.add_widget(self.Gridlayout_teach_history)
        
        self.remark_teach_issue=CardHolder(size_hint=(1,.33))
        self.remark_teach_issue.ids.lbltitle.text='Remarks'
        self.txt_remarks_teach=TextInput(multiline=True,size_hint=(1,1),hint_text='Type remarks here', background_color = (1,1,1,0),\
                                   background_normal = '', background_active = '', cursor_color = (0/255, 109/255, 240/255, 1),hint_text_color=(0,0,0,.8))
        
        self.remark_teach_issue.ids.boxl.add_widget(self.txt_remarks_teach)
        self.remark_teach_issue.ids.boxl.padding=(20,0,20,0)
        self.ref_remarks_teach=IconButton(text =u'\uF450',font_size='24sp', size=(48,48),pos_hint={'center_x':.9,'center_y':.5},theme_text_color='Custom',text_color=(0,0,0,.5))
        self.remark_teach_issue.ids.float1.add_widget(self.ref_remarks_teach)

        #search tab borrow
        self.searchtab_teach_borrow=Search_Tab(size_hint=(1,.09),size=(600,60), pos_hint={'center_x':.5,'center_y':1})
        #search tab history
        self.searchtab_teach_history=Search_Tab(size_hint=(1,.09),size=(600,60), pos_hint={'center_x':.5,'center_y':1})

        self.boxl_teach0 = BoxLayout(padding = (20,20,20,20), spacing = 20)
        self.boxl_teach1 = BoxLayout(spacing = 20, orientation = 'vertical', size_hint_x = .4)
        self.boxl_teach2 = BoxLayout(size_hint_x = .6, padding = (0,0,0,40))
        self.boxl_teach1.add_widget(self.img_teachers_issue)
        self.boxl_teach1.add_widget(self.remark_teach_issue)
        self.boxl_teach2.add_widget(self.nav_teachers_issue)
        self.boxl_teach0.add_widget(self.boxl_teach1)
        self.boxl_teach0.add_widget(self.boxl_teach2)
        self.boxl_teach3 = BoxLayout(size_hint_y=None,height=dp(600),padding = (20,20,20,20), spacing = 20, orientation='vertical')
        self.boxl_teach4 = BoxLayout(size_hint_y=None,height=dp(600),padding = (20,20,20,20), spacing = 20, orientation='vertical')
        self.boxl_teach3.add_widget(self.searchtab_teach_borrow)
        self.boxl_teach3.add_widget(self.current_Teachers_issue)
        self.boxl_teach4.add_widget(self.searchtab_teach_history)
        self.boxl_teach4.add_widget(self.history_teach_issue)

        #nav
        scrll_nav1 = ScrollView(scroll_type=['bars'], bar_width = dp(15),bar_color=( 0, 52/255, 102/255, 1))
        box_nav1 =BoxWhite(size_hint_y=None, orientation='vertical')
        box_nav1.bind(minimum_height=box_nav1.setter('height'))
        scrll_nav1.add_widget(box_nav1)
        
        box_nav1.add_widget(self.boxl_teach3)
        box_nav1.add_widget(self.boxl_teach4)

        self.ids.stack_Teachers_borro_ret.add_widget(scrll_nav1)
        self.ids.stack_Teachers_borro_ret.add_widget(self.boxl_teach0)

        
        #get scroll and inputs
        self.wid_teach_circ_scrolls=self.nav_teachers_issue.get_scroll_input()
        self.wid_teach_circ_input=self.nav_teachers_issue.get_nav_buttons()

        #search for history
        self.searchtab_teach_history.ids.btn.bind(on_press=partial(self.do_search_for_records_circ, self.wid_teach_circ_scrolls, self.searchtab_teach_history.ids.txt, \
                                                                 None, self.Gridlayout_teach_history,'t','hst'))
        self.searchtab_teach_history.ids.txt.bind(on_text_validate=partial(self.do_search_for_records_circ, self.wid_teach_circ_scrolls, self.searchtab_teach_history.ids.txt, \
                                                               None, self.Gridlayout_teach_history,'t','hst'))
        
        #search for borrow
        self.searchtab_teach_borrow.ids.btn.bind(on_press=partial(self.do_search_for_records_circ, self.wid_teach_circ_scrolls, self.searchtab_teach_borrow.ids.txt, \
                                                                 self.Gridlayout_teach_issue, None,'t','br'))
        self.searchtab_teach_borrow.ids.txt.bind(on_text_validate=partial(self.do_search_for_records_circ, self.wid_teach_circ_scrolls, self.searchtab_teach_borrow.ids.txt, \
                                                               self.Gridlayout_teach_issue, None,'t','br'))

        #show menu act/deact
        self.actd_teach.bind(on_press=partial(self.to_deactivate_member,self.wid_teach_circ_scrolls, 't','deactivate'))
        self.actd_teach0.bind(on_press=partial(self.to_deactivate_member,self.wid_teach_circ_scrolls, 't','activate'))
        #refresh remarks
        self.ref_remarks_teach.bind(on_press=partial(self.update_remarks,self.wid_teach_circ_scrolls,'t'))
        
        #search bindings
        self.wid_teach_circ_scrolls['id_no'].bind(on_text_validate=partial(self.teach_search_circ,self.txt_remarks_teach))
        self.wid_teach_circ_scrolls['book_acc_no'].bind(on_text_validate=self.book_search_circ_for_teach)
        
        #clear
        self.wid_teach_circ_input['clear_f'].bind(on_press=partial(self.clear_form_circ,self.wid_teach_circ_scrolls,'t' ))                                                 
        #update
        self.wid_teach_circ_input['update'].bind(on_press=partial(self.update_record_circ,self.wid_teach_circ_scrolls ))
        #first
        self.wid_teach_circ_input['first_r'].bind(on_press=partial(self.move_to_first_record_circ,self.wid_teach_circ_scrolls,\
                                                                     self.nav_teachers_issue,'t'))
        #previous
        self.wid_teach_circ_input['prev_r'].bind(on_press=partial(self.move_to_prev_record_circ,self.wid_teach_circ_scrolls,\
                                                                     self.nav_teachers_issue,'t'))
        #add record
        self.wid_teach_circ_input['add_r'].bind(on_press=partial(self.combined_circ_add_rec, self.wid_teach_circ_scrolls, self.nav_teachers_issue,\
                                                               self.wid_teach_circ_input, 't'))
        #next
        self.wid_teach_circ_input['next_r'].bind(on_press=partial(self.move_to_next_record_circ,self.wid_teach_circ_scrolls,\
                                                                     self.nav_teachers_issue,'t'))
        #last
        self.wid_teach_circ_input['last_r'].bind(on_press=partial(self.move_to_last_record_circ,self.wid_teach_circ_scrolls,\
                                                                     self.nav_teachers_issue,'t'))
        self.wid_teach_circ_input['del_r'].disabled=True

        #add widgets for non teaching stuff issue and return
        self.img_non_teaching_issue=Imageframe(source='pics\\account.png',size_hint=(1,.6))
        self.nav_non_teaching_issue=Navigator(which_scroll='non_teaching_issue')
        self.actd_non0=IconButton\
                        (text =u'\uF33F',font_size='24sp',x=self.actd_std.x,\
                                size=(48,48),color=(0,0,0,.63),pos_hint={'right':.9,'center_y':.5})
        self.nav_non_teaching_issue.ids.float1.add_widget(self.actd_non0)
        self.actd_non=IconButton(text =u'\uF33E',font_size='24sp',size=(48,48),color=(0,0,0,.63),pos_hint={'right':.97,'center_y':.5})
        self.nav_non_teaching_issue.ids.float1.add_widget(self.actd_non)
        
        self.nav_non_teaching_issue.ids.lbltitle.text='Non teaching stuff book circulation form'
        self.current_non_issue=CardHolder(size_hint=(1,.84))
        self.current_non_issue.ids.lbltitle.text='Current borrowed books'
        #add scroll to non teacher borrow
        scroll_widget_non_issue=ScrollView(size_hint=(1,1))
        self.current_non_issue.ids.boxl.add_widget(scroll_widget_non_issue)
        self.Gridlayout_non_issue=GridLayout(cols=1,spacing=20,size_hint_y=None,padding=(5,5,5,10))
        self.Gridlayout_non_issue.bind(minimum_height=self.Gridlayout_non_issue.setter('height'))
        scroll_widget_non_issue.add_widget(self.Gridlayout_non_issue)
        
        self.history_non_issue=CardHolder(size_hint=(1,.84))
        self.history_non_issue.ids.lbltitle.text='History of books'
       # self.ref_history_non=Button(background_normal ='refresh',pos_hint={'center_x':.9,'center_y':.5},theme_text_color='Custom',text_color=(0,0,0,.5))
       # self.history_non_issue.ids.float1.add_widget(self.ref_history_non)
       # self.ref_history_non.bind(on_press=partial(self.show_history_books,'n'))
        
        #add scroll for history
        scroll_widget_non_history=ScrollView(size_hint=(1,1))
        self.history_non_issue.ids.boxl.add_widget(scroll_widget_non_history)
        self.Gridlayout_non_history=GridLayout(cols=1,spacing=10,size_hint_y=None,padding=(5,5,5,5))
        self.Gridlayout_non_history.bind(minimum_height=self.Gridlayout_non_history.setter('height'))
        scroll_widget_non_history.add_widget(self.Gridlayout_non_history)
        
        self.remark_non_issue=CardHolder(size_hint=(1,.33))
        self.remark_non_issue.ids.lbltitle.text='Remarks'
        self.txt_remarks_non=TextInput(multiline=True,size_hint=(1,1),hint_text='Type remarks here', background_color = (1,1,1,0),\
                                   background_normal = '', background_active = '', cursor_color = (0/255, 109/255, 240/255, 1),hint_text_color=(0,0,0,.8))
        
        self.ref_rmarks=IconButton(text =u'\uF450',font_size='24sp', size=(48,48),pos_hint={'center_x':.9,'center_y':.5},theme_text_color='Custom',text_color=(0,0,0,.5))
        self.remark_non_issue.ids.float1.add_widget(self.ref_rmarks)
        self.remark_non_issue.ids.boxl.add_widget(self.txt_remarks_non)
        self.remark_non_issue.ids.boxl.padding=(20,0,20,0)

        #search tab borrow
        self.searchtab_non_borrow=Search_Tab(size_hint=(1,.09),size=(600,60), pos_hint={'center_x':.5,'center_y':1})
        #search tab history
        self.searchtab_non_history=Search_Tab(size_hint=(1,.09),size=(600,60), pos_hint={'center_x':.5,'center_y':1})

        self.boxl_non0 = BoxLayout(padding = (20,20,20,20), spacing = 20)
        self.boxl_non1 = BoxLayout(spacing = 20, orientation = 'vertical', size_hint_x = .4)
        self.boxl_non2 = BoxLayout(size_hint_x = .6, padding = (0,0,0,40))
        self.boxl_non1.add_widget(self.img_non_teaching_issue)
        self.boxl_non1.add_widget(self.remark_non_issue)
        self.boxl_non2.add_widget(self.nav_non_teaching_issue)
        self.boxl_non0.add_widget(self.boxl_non1)
        self.boxl_non0.add_widget(self.boxl_non2)
        self.boxl_non3 = BoxLayout(size_hint_y=None, height=dp(600),padding = (20,20,20,20), spacing = 20, orientation='vertical')
        self.boxl_non4 = BoxLayout(size_hint_y=None, height=dp(600),padding = (20,20,20,20), spacing = 20, orientation='vertical')
        self.boxl_non3.add_widget(self.searchtab_non_borrow)
        self.boxl_non3.add_widget(self.current_non_issue)
        self.boxl_non4.add_widget(self.searchtab_non_history)
        self.boxl_non4.add_widget(self.history_non_issue)


        #nav
        scrll_nav2 = ScrollView(scroll_type=['bars'], bar_width = dp(15),bar_color=( 0, 52/255, 102/255, 1))
        box_nav2 =BoxWhite(size_hint_y=None, orientation='vertical')
        box_nav2.bind(minimum_height=box_nav2.setter('height'))
        scrll_nav2.add_widget(box_nav2)
        
        box_nav2.add_widget(self.boxl_non3)
        box_nav2.add_widget(self.boxl_non4)

        self.ids.stack_non_teaching_borro_ret.add_widget(scrll_nav2)
        self.ids.stack_non_teaching_borro_ret.add_widget(self.boxl_non0)
        
        
        #get scroll and inputs
        self.wid_non_circ_scrolls=self.nav_non_teaching_issue.get_scroll_input()
        self.wid_non_circ_input=self.nav_non_teaching_issue.get_nav_buttons()

        #search bindings
        self.wid_non_circ_scrolls['id_no'].bind(on_text_validate=partial(self.non_search_circ,self.txt_remarks_non))
        self.wid_non_circ_scrolls['book_acc_no'].bind(on_text_validate=self.book_search_circ_for_non)

        #search for history
        self.searchtab_non_history.ids.btn.bind(on_press=partial(self.do_search_for_records_circ, self.wid_non_circ_scrolls, self.searchtab_non_history.ids.txt, \
                                                                 None, self.Gridlayout_non_history,'n','hst'))
        self.searchtab_non_history.ids.txt.bind(on_text_validate=partial(self.do_search_for_records_circ, self.wid_non_circ_scrolls, self.searchtab_non_history.ids.txt, \
                                                               None, self.Gridlayout_non_history,'n','hst'))
        
        #search for borrow
        self.searchtab_non_borrow.ids.btn.bind(on_press=partial(self.do_search_for_records_circ, self.wid_non_circ_scrolls, self.searchtab_non_borrow.ids.txt, \
                                                                 self.Gridlayout_non_issue, None,'n','br'))
        self.searchtab_non_borrow.ids.txt.bind(on_text_validate=partial(self.do_search_for_records_circ, self.wid_non_circ_scrolls, self.searchtab_non_borrow.ids.txt, \
                                                               self.Gridlayout_non_issue, None,'n','br'))

        #show menu act/deact
        self.actd_non.bind(on_press=partial(self.to_deactivate_member,self.wid_non_circ_scrolls, 'n','deactivate'))
        self.actd_non0.bind(on_press=partial(self.to_deactivate_member,self.wid_non_circ_scrolls, 'n','activate'))
        #refresh remarks
        self.ref_rmarks.bind(on_press=partial(self.update_remarks,self.wid_non_circ_scrolls,'n'))
        #clear
        self.wid_non_circ_input['clear_f'].bind(on_press=partial(self.clear_form_circ,self.wid_non_circ_scrolls,'n' ))                                                 
        #update
        self.wid_non_circ_input['update'].bind(on_press=partial(self.update_record_circ,self.wid_non_circ_scrolls ))
        #first
        self.wid_non_circ_input['first_r'].bind(on_press=partial(self.move_to_first_record_circ,self.wid_non_circ_scrolls,\
                                                                     self.nav_non_teaching_issue,'n'))
        #previous
        self.wid_non_circ_input['prev_r'].bind(on_press=partial(self.move_to_prev_record_circ,self.wid_non_circ_scrolls,\
                                                                     self.nav_non_teaching_issue,'n'))
        #add record
        self.wid_non_circ_input['add_r'].bind(on_press=partial(self.combined_circ_add_rec, self.wid_non_circ_scrolls, self.nav_non_teaching_issue,\
                                                               self.wid_non_circ_input, 'n'))
        #next
        self.wid_non_circ_input['next_r'].bind(on_press=partial(self.move_to_next_record_circ,self.wid_non_circ_scrolls,\
                                                                     self.nav_non_teaching_issue,'n'))
        #last
        self.wid_non_circ_input['last_r'].bind(on_press=partial(self.move_to_last_record_circ,self.wid_non_circ_scrolls,\
                                                                     self.nav_non_teaching_issue,'n'))
        self.wid_non_circ_input['del_r'].disabled=True


        ####################### ONLINE SCROLLVIEW FOR BOOKS #########################
        #initializing scroll to cardholder
        self.scroll_widget=ScrollView(size_hint=(1,1),bar_width=0)
        self.scroll_online=GridLayout(cols=1, spacing=10, size_hint_y=(None),padding=(20,20,20,20))
        self.scroll_online.bind(minimum_height=self.scroll_online.setter('height'))
        self.scroll_widget.add_widget(self.scroll_online)
        self.cardholder_bk_reg.ids.boxl.add_widget(self.scroll_widget)

        ####################### NOTIFICATIONS FOR BOOKS #########################
        # refresh the date passed
        self.timer_start_work_notification()
        #refresh the notification controls contents
        Clock.schedule_interval(self.update_cards_content,10)
        #change the cards
        Clock.schedule_interval(self.change_cards,10)
        self.screen_list=[0,1,2,3]

        ##################### BACKUP FOR DATABASE ##########################
        #Check for a backup
        Clock.schedule_interval(self.do_backup,60)

        ##################### LOGIN ##########################
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        try:
            #check whether the reg path exists
            aKey=OpenKey(aReg, r"SOFTWARE\LibrarySystem\accounts", 0, KEY_ALL_ACCESS)
        except FileNotFoundError:
            # if not create the path plus add the default account
            aKey = CreateKeyEx(aReg, r"SOFTWARE\LibrarySystem\accounts", 0, KEY_ALL_ACCESS) 
            SetValueEx(aKey,"accounts",0, REG_SZ, str({'Administrator':'ron'})) 
        CloseKey(aKey)

        self.populate_users()
        ##################### DASHBOARD ##########################
        #Check the total number of books
        Clock.schedule_interval(self.refresh_total_no_books,5)

        ##################### BARCODE ##########################
        self.index_preview=0
        
        self.ids.margin_x.text = str(self.page_settings['margin_x'])
        self.ids.margin_y.text = str(self.page_settings['margin_y'])
        self.ids.nocpp.text = str(self.page_settings['cols'])
        self.ids.norpp.text = str(self.page_settings['rows'])
        self.ids.sbbx.text = str(self.page_settings['space_x'])
        self.ids.sbby.text = str(self.page_settings['space_y'])

        ##################### BARCODE SCANNER ##########################
        self.full_no=''
        Window.bind(on_key_down=self._on_key_down)
        ##################### REPORTS & PRINTING ##########################
        self.index_preview_reports = 0

        ##################### LOAD THEME ##########################
        self.load_theme()
        
        ##################### CALCULATE DATE ##########################
        #self.calc_date()

##    def calc_date(self):
##        self.nav_std_issue.ids
##        self.nav_teachers_issue
##        self.nav_non_teaching_issue

    def register_app(self,one, two, three, four):
        print(one, two, three, four)
        if str(one) =='2' and str(two) =='0' and str(three)=='0' and str(four) =='0':
            content = MDLabel(font_style='Caption',text="Correct key",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Successfully!",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
            
            self.current =='main'
            file = open('pky.dat','w')
            file.write(one+two+three+four)
            file.close()
        else:
            content = MDLabel(font_style='Caption',text="Key mismatch",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Warning!",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()

    ########################### POINTER MOVEMENT ##############################
    def change_pointer(self, inst):
        self.pointer_movent = inst
          
    ########################### SET THEME ##############################
    def load_theme(self):
        existing=[]
        for filename in glob.iglob('*.txt'):
             existing.append(filename)

        #check the theme
        if 'theme.txt' not in existing:
            file=open('theme.txt','w')
            file.write('None')
            path = None
        elif 'theme.txt' in existing:
            file=open('theme.txt','r')
            path=file.read()
        file.close()

        if path == 'None':
            self.set_theme(None)
            self.line_nav=False
        else:
            if path == 'pics\\water1.zip':
                self.set_theme(self.ids.tgle_water)
            elif path == 'pics\\nature.zip':
                self.set_theme(self.ids.tgle_nature)
            elif path == 'pics\\book.zip':
                self.set_theme(self.ids.tgle_book)
            elif path == 'pics\\tech.zip':
                self.set_theme(self.ids.tgle_tech)
            elif path == 'pics\\stream.zip':
                self.set_theme(self.ids.tgle_stream)
            elif path == 'pics\\blur.jpg':
                self.set_theme(self.ids.tgle_blur)
            elif path == 'pics\\blur.jpg2':
                self.set_theme(self.ids.tgle_blur2)
            self.line_nav=True
                
        
    def set_theme(self, inst):
        if inst == None:
            rectangle=self.canvas.get_group('h')[1]
            if hasattr(self, 'img_texture'):
                self.img_texture.unbind(texture=partial(self.change_text,rectangle))
                content = MDLabel(font_style='Caption',text="You need to restart the application.",\
                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Message",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
                
            rectangle.texture =None

            file=open('theme.txt','w')
            file.write('None')
            file.close()

            self.line_nav=True
        else:
            rectangle=self.canvas.get_group('h')[1]
            self.img_texture = Image(source = inst.source, mipmap=True,anim_delay=0.1)
            rectangle.texture = self.img_texture.texture
            self.img_texture.bind(texture=partial(self.change_text,rectangle))

            file=open('theme.txt','w')
            file.write(str(inst.source))
            file.close()
            self.line_nav=False


    def change_text(self, rec, *args):
        rec.texture = self.img_texture.texture

    def change_crr(self, inst,*args):
        if inst.index==0:
            self.ids.ttl_one.state='down'
            self.ids.ttl_mass.state='normal'
        else:
            self.ids.ttl_one.state='normal'
            self.ids.ttl_mass.state='down'
        
    ################################################################# TEXT TO RECORDS
    def reset_appended_rec(self):
        self.rst_records=[]
        self.ids.rst_doc.text = ''
        
    def ShowPreview(self):
        records = self.ids.t2r_line_txt.text.split(self.ids.t2r_sep_txt.text)
        
        if len(records) ==9:
            self.rst_records.append(records)
            #draw a line
            dashes = '-'*13*9+'+'
            for i in range(0, len(dashes), 13):
                dashes =dashes[:i]+'+'+dashes[i+1:]
                
            #enter a record
            headers=['isbn', 'title', 'publisher', 'edition', 'author', 'place of publication', 'year of publication', 'category', 'shelve no']
            borders = '|'*13*9
            c=0
            for i in range(1, len(borders), 13):
                word = headers[c]+' '*(12-len(headers[c])) if len(headers[c]) <=12 else headers[c][:9]+'...'
                borders = borders[:i]+word+borders[i+12:]
                c+=1
            borders = borders+'|'
            #draw a line
            equals = '='*13*9+'+'
            for i in range(0, len(equals), 13):
                equals =equals[:i]+'+'+equals[i+1:]

            if self.ids.rst_doc.text != '':
                pass
            else:
                #create a header
                self.ids.rst_doc.text = dashes+"\n"+borders+"\n"+equals

            #add record
            c=0
            rec = '|'*13*9
            for i in range(1, len(borders), 13):
                word = records[c]+' '*(12-len(records[c])) if len(records[c]) <=12 else records[c][:9]+'...'
                rec = rec[:i]+word+rec[i+12:]
                c+=1
            rec = rec+'|'

            self.ids.rst_doc.text +="\n"+rec+"\n"+dashes

            self.ids.t2r_line_txt.text = ''
            
        self.ids.t2r_line_txt.focus=True
            
    def add_appended_rec(self):
        if len(self.rst_records)>0:
            #calculate the next id number
            self.cursor.execute(''' SELECT book_accession_no FROM books ''')
            acc_rec=self.cursor.fetchall()
            last_rec_no=len(acc_rec)
            if last_rec_no==0:
                rec_no=1
            else:
                rec_no=acc_rec[last_rec_no-1][0]
                
            for rec in self.rst_records:
                rec_no+=1                
                self.cursor.execute('''INSERT INTO books(isbn,title,publisher,edition,author,place_of_publication,year_of_publication,category,\
                                                            shelve_no,by_user,id, lost, lost_by, borrowed, borrowed_by,damaged,damaged_by)\
                                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',\
                                    (rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8],self.user_name,rec_no, 'no', 'none', 'no', 'none', 'no', 'none',))

                self.connection.commit()
                
        self.ids.t2r_line_txt.text = ''
        self.ids.rst_doc.text = ''
        self.rst_records = []
        self.ids.t2r_line_txt.focus=True
                    
    ################################################################## BARCODE SCANNER DETECTION
    def _on_key_down(self, instance, key, scancode, codepoint, modifier):
            if key == 13 and scancode == 40:
                #make sure the user is in the current page
                if self.ids.sm_content.current=='barcode_ret':
                    #return using the admission number
                    self.cursor.execute(''' SELECT lost,lost_by FROM books WHERE book_accession_no=? ''',( self.full_no,))
                    lost=self.cursor.fetchall()

                    if len(lost)>0:
                        if lost[0][0]=='yes':
                            self.ids.rv_ret.data.insert(0, {'text': 'Book accession number %s is lost by %s '%(self.full_no, lost[0][1])})
                        else:
                            self.cursor.execute(''' SELECT damaged, damaged_by FROM books WHERE book_accession_no=? ''',(self.full_no,))
                            damaged = self.cursor.fetchall()

                            if damaged[0][0]=='yes':
                                #show message for book is damaged
                                self.ids.rv_ret.data.insert(0, {'text': 'Book accession number  %s is damaged by %s '%(self.full_no, damaged[0][1])})
                            else:
                                #check if the book is borrowed
                                self.cursor.execute(''' SELECT borrowed FROM books WHERE book_accession_no = ? ''',(self.full_no,))
                                borro=self.cursor.fetchall()
                                
                                if borro[0][0]=='no':
                                    self.ids.rv_ret.data.insert(0, {'text': 'Book accession number %s is not borrowed'%self.full_no})
                                elif borro[0][0]=='yes':
                                    #fetch the adm/adm/no
                                    self.cursor.execute(''' SELECT * FROM borrow WHERE book_accession_no = ? ''',(self.full_no,))
                                    mtype = self.cursor.fetchall()
                                    #update book as not borrowed
                                    self.cursor.execute(''' UPDATE books SET borrowed='no', borrowed_by='none' WHERE book_accession_no = ? ''',(self.full_no,))
                                    self.connection.commit()
                                    #delete member borrowing record
                                    self.cursor.execute(''' DELETE FROM borrow WHERE book_accession_no=? ''',(self.full_no,))
                                    self.connection.commit()
                                    #add record to history
                                    today_date=str(datetime.datetime.now())[:10]
                                    self.cursor.execute(''' INSERT INTO history(book_accession_no, adm_no, id_no,  date_issued, date_suppossed_return, date_returned, date_passed_by, by_user)\
                                                                VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',\
                                                            (mtype[0][7], mtype[0][1], mtype[0][2], mtype[0][3], mtype[0][4], today_date, mtype[0][6], self.user_name,))
                                    self.connection.commit()
                                    if mtype[0][8]=='student':
                                        self.ids.rv_ret.data.insert(0, {'text': 'Book accession number %s is successfully returned by %s'%(self.full_no, mtype[0][1])})
                                    else:
                                        self.ids.rv_ret.data.insert(0, {'text': 'Book accession number %s is successfully returned by %s'%(self.full_no, mtype[0][2])})

                self.full_no=''
                
            else:
                self.full_no+= str(codepoint)
            

    ################################################################## REPORTS AND PRINTING
    def go_to_page(self,txt):
        files = glob.glob('reports\\reports_images\\*')
        txt=int(txt)-1
        if 'reports\\reports_images\\img-%s.png'%txt not in files:
            content = MDLabel(font_style='Caption',text="The number should be between 1 - %s "%len(files),\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Page not found",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialo()
        else:
            self.ids.img_preview_reports.source='reports\\reports_images\\img-%s.png'%txt
            self.ids.img_preview_reports.reload()
            self.ids.lbl_preview_reports.text='[b]Page(s): %s/%s[/b]'%(txt+1,len(files))
            
    def move_preview_img_reports(self,nop):
        existing=[]
        for filename in glob.iglob('reports\\reports_images\\*.png'):
             existing.append(filename)
        
        if nop=='n':
            if (self.index_preview_reports+1) <= len(existing)-1:
                self.index_preview_reports+=1
                self.ids.img_preview_reports.source=existing[self.index_preview_reports]
                self.ids.img_preview_reports.reload()
                self.ids.lbl_preview_reports.text='[b]Page(s): %s/%s[/b]'%(self.index_preview_reports+1,len(existing))
        else:
            if (self.index_preview_reports-1) >= 0:
                self.index_preview_reports -=1
                self.ids.img_preview_reports.source=existing[self.index_preview_reports]
                self.ids.img_preview_reports.reload()
                self.ids.lbl_preview_reports.text='[b]Page(s): %s/%s[/b]'%(self.index_preview_reports+1,len(existing))
        
    def preview_reports_0(self):
        existing=[]
        for filename in glob.iglob('reports\\*.pdf'):
             existing.append(filename)
        #check if the generated barcode.pdf exists
        if 'reports\\report.pdf' not in existing:
            content = MDLabel(font_style='Caption',text="Generate a report first to proceed",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Nothing to print",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            files = glob.glob('reports\\reports_images\\*')
            
            if len(files)==0:
                self.ids.img_preview_reports.source='pics\\no_preview.png'
                self.ids.lbl_preview_reports.text='[b]Page(s): 0/%s[/b]'%len(files)
            else:
                #view pictures on the screen manager
                self.ids.img_preview_reports.source=files[0]
                self.ids.img_preview_reports.reload()
                self.ids.lbl_preview_reports.text='[b]Page(s): 1/%s[/b]'%len(files)
                
            self.index_preview_reports=0
   
    def print_file_reports(self):
        existing=[]
        for filename in glob.iglob('reports\\*.pdf'):
             existing.append(filename)

        #check if the generated barcode.pdf exists
        if 'reports\\report.pdf' not in existing:
            content = MDLabel(font_style='Caption',text="Generate a report first to proceed",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Nothing to print",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            
            try:
                current =  os.getcwd()
                filename = current+'\\reports\\report.pdf'
                win32api.ShellExecute ( 0,"print",filename,
                 
                  '/c:"%s"' % win32print.GetDefaultPrinter (),
                  ".",
                  0
                )
            except:
                content = MDLabel(font_style='Caption',text="Ensure you have connected the printer you want to print with then proceed with printing",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Printer error !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()

                
    def generate_reports(self, title, box, tel, motto, subtitle, message):

        if self.ids.chkbx_lost.active== True:
            #select only distict details adm and ids
            self.cursor.execute(''' SELECT DISTINCT lost_by FROM books WHERE lost='yes' ORDER BY lost_by ASC''')
            distinct_lost_rec=self.cursor.fetchall()

            #check if there is nothing to generate
            if len(distinct_lost_rec) >0:
                c = canvas.Canvas('reports\\report.pdf',pagesize=A4)
                for each_distinct_rec in distinct_lost_rec:
                    width, height= A4
                    #Draw title
                    c.setFont('Helvetica-Bold', 24)
                    c.drawCentredString( width/2, height-70, title)
                    #Draw P.O BOX
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-90, 'P.O BOX : %s'%box)
                    #Draw telephone number
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-110, 'Tel : %s'%tel)
                    #Draw school motto
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-130, 'Motto : %s'%motto)
                    #Draw the lions logo
                    c.drawImage('pics\\logo.jpg', 50, height-130, 60, 60)
                    #Draw line
                    c.setLineWidth(2)
                    c.line( 25, height-150 , width-25, height-150)
                    #Draw subtitle
                    c.setFont('Helvetica', 13)
                    c.drawCentredString(width/2, height-170, subtitle)
                    #Greetings "Dear"
                    c.setFont('Helvetica', 10)
                    c.drawString(50, height-240, 'Dear Sir/Madam ,')

                    #Body 
                    #select every book the person has lost
                    self.cursor.execute(''' SELECT title,publisher FROM books WHERE lost_by=? ''', (each_distinct_rec[0],))
                    all_lost_rec=self.cursor.fetchall()
                
                    textobj = c.beginText()
                    textobj.setTextOrigin( 50, height-280)
                    textobj.setFont('Helvetica', 10)
                    wraped_text = "\n".join(wrap(message,110))
                    textobj.textLines(wraped_text)
                    lost_book_message='The following books should be replaced :'
                    textobj.textLine(lost_book_message)
                    counter=0
                    for each_lost_book in all_lost_rec:
                        counter+=1
                        messages= str(counter)+'. '+str(each_lost_book[0])+' (book publisher: %s )'%str(each_lost_book[1])
                        #draw the paragraph
                        textobj.textLine(messages)
                    c.drawText(textobj)

                    c.setDash(1,2)
                    c.setLineWidth(1)
                    #shows to who ?
                    self.cursor.execute(''' SELECT class FROM members WHERE adm_no IS ? OR id_no IS? ''',(each_distinct_rec[0], each_distinct_rec[0],))
                    clas = self.cursor.fetchall()
                    print(clas)
                    c.setFont('Helvetica', 10)
                    c.drawString(50, 260, 'To : %s class : %s'%(each_distinct_rec[0], clas[0][0]))
                    #Draw line to adm or id
                    c.setLineWidth(1)
                    c.line( 80, 255 , 90, 255)
                    #Draw line to class
                    c.setLineWidth(1)
                    c.line( 130, 255 , 170, 255)
                    #shows to who ?
                    c.setFont('Helvetica', 10)
                    c.drawString(50, 220, 'Served by : %s'%self.user_name)
        
                    c.showPage()
                c.save()
                #clean the files for new pictures
                files = glob.glob('reports\\reports_images\\*')
                for f in files:
                    os.remove(f)
                    
                #generate pictures
                cpath = os.path.dirname(__file__)
                os.startfile('generate_reports.bat')
                
                content = MDLabel(font_style='Caption',text="reports generated successfully",\
                                  size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Reports generated",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
            else:
                content = MDLabel(font_style='Caption',text="No reports to generate",\
                                  size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="No reports",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
                
        elif self.ids.chkbx_damaged.active== True:
            #select only distict details adm and ids
            self.cursor.execute(''' SELECT DISTINCT damaged_by FROM books WHERE damaged='yes' ORDER BY damaged_by ASC''')
            distinct_damaged_rec=self.cursor.fetchall()
            if len(distinct_damaged_rec)>0:
                c = canvas.Canvas('reports\\report.pdf',pagesize=A4)
                for each_distinct_rec in distinct_damaged_rec:
                    width, height= A4
                    #Draw title
                    c.setFont('Helvetica-Bold', 24)
                    c.drawCentredString( width/2, height-70, title)
                    #Draw P.O BOX
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-90, 'P.O BOX : %s'%box)
                    #Draw telephone number
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-110, 'Tel : %s'%tel)
                    #Draw school motto
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-130, 'Motto : %s'%motto)
                    #Draw the lions logo
                    c.drawImage('pics\\logo.jpg', 50, height-130, 60, 60)
                    #Draw line
                    c.setLineWidth(2)
                    c.line( 25, height-150 , width-25, height-150)
                    #Draw subtitle
                    c.setFont('Helvetica', 13)
                    c.drawCentredString(width/2, height-170, subtitle)
                    #Greetings "Dear"
                    c.setFont('Helvetica', 10)
                    c.drawString(50, height-240, 'Dear Sir/Madam ,')

                    #Body 
                    #select every book the person has lost
                    self.cursor.execute(''' SELECT title,publisher FROM books WHERE damaged_by=? ''', (each_distinct_rec[0],))
                    all_damaged_rec=self.cursor.fetchall()
                    
                    textobj = c.beginText()
                    textobj.setTextOrigin( 50, height-280)
                    textobj.setFont('Helvetica', 10)
                    wraped_text = "\n".join(wrap(message,110))
                    textobj.textLines(wraped_text)
                    damaged_book_message='The following books were damaged and should be replaced :'
                    textobj.textLine(damaged_book_message)
                    counter=0
                    for each_damaged_book in all_damaged_rec:
                        counter+=1
                        messages= str(counter)+'. '+str(each_damaged_book[0])+' (book publisher: %s )'%str(each_damaged_book[1])
                        #draw the paragraph
                        textobj.textLine(messages)
                    c.drawText(textobj)

                    c.setDash(1,2)
                    c.setLineWidth(1)
                    #shows to who ?
                    self.cursor.execute(''' SELECT class FROM members WHERE adm_no IS ? OR id_no IS ?  ''',(each_distinct_rec[0], each_distinct_rec[0],))
                    clas = self.cursor.fetchall()
                    c.setFont('Helvetica', 10)
                    c.drawString(50, 260, 'To : %s class : %s'%(each_distinct_rec[0], clas[0][0]))
                    #Draw line to adm or id
                    c.setLineWidth(1)
                    c.line( 80, 255 , 90, 255)
                    #Draw line to class
                    c.setLineWidth(1)
                    c.line( 130, 255 , 170, 255)
                    #shows to who ?
                    c.setFont('Helvetica', 10)
                    c.drawString(50, 220, 'Served by : %s'%self.user_name)
        
                    c.showPage()
                c.save()
                #clean the files for new pictures
                files = glob.glob('reports\\reports_images\\*')
                for f in files:
                    os.remove(f)
                    
                #generate pictures
                cpath = os.path.dirname(__file__)
                os.startfile('generate_reports.bat')
                
                content = MDLabel(font_style='Caption',text="reports generated successfully",\
                                  size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Reports generated",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
            else:
                content = MDLabel(font_style='Caption',text="No reports to generate",\
                                  size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="No reports",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
                
        elif self.ids.chkbx_return.active== True:
            #select only distict details adm and ids
            self.cursor.execute(''' SELECT DISTINCT adm_no, id_no FROM borrow WHERE date_passed_by > 0 ''')
            distinct_not_ret_rec=self.cursor.fetchall()
            print(distinct_not_ret_rec)
            if len(distinct_not_ret_rec)>0:
                c = canvas.Canvas('reports\\report.pdf',pagesize=A4)
                for each_distinct_rec in distinct_not_ret_rec:
                    width, height= A4
                    #Draw title
                    c.setFont('Helvetica-Bold', 24)
                    c.drawCentredString( width/2, height-70, title)
                    #Draw P.O BOX
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-90, 'P.O BOX : %s'%box)
                    #Draw telephone number
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-110, 'Tel : %s'%tel)
                    #Draw school motto
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString( width/2-50, height-130, 'Motto : %s'%motto)
                    #Draw the lions logo
                    c.drawImage('pics\\logo.jpg', 50, height-130, 60, 60)
                    #Draw line
                    c.setLineWidth(2)
                    c.line( 25, height-150 , width-25, height-150)
                    #Draw subtitle
                    c.setFont('Helvetica', 13)
                    c.drawCentredString(width/2, height-170, subtitle)
                    #Greetings "Dear"
                    c.setFont('Helvetica', 10)
                    c.drawString(50, height-240, 'Dear Sir/Madam ,')

                    #Body 
                    #select every book the person has lost
                    if each_distinct_rec[0]=='none':
                        self.cursor.execute(''' SELECT title,publisher FROM books WHERE borrowed_by=? ''', (each_distinct_rec[1],))
                    else:
                        self.cursor.execute(''' SELECT title,publisher FROM books WHERE borrowed_by=? ''', (each_distinct_rec[0],))
                    all_not_ret_rec=self.cursor.fetchall()
                    
                    textobj = c.beginText()
                    textobj.setTextOrigin( 50, height-280)
                    textobj.setFont('Helvetica', 10)
                    wraped_text = "\n".join(wrap(message,110))
                    textobj.textLines(wraped_text)
                    not_ret_book_message='The following book(s) should be returned :'
                    textobj.textLine(not_ret_book_message)
                    counter=0
                    for each_not_ret_book in all_not_ret_rec:
                        counter+=1
                        messages = str(counter)+'. '+str(each_not_ret_book[0])+' (book publisher: %s )'%str(each_not_ret_book[1])
                        #draw the paragraph
                        textobj.textLine(messages)
                        
                    c.drawText(textobj)
                    c.setDash(1,2)
                    c.setLineWidth(1)
                    #shows to who ?
                    self.cursor.execute(''' SELECT class FROM members WHERE adm_no IS ? OR id_no IS ?  ''',(each_distinct_rec[0], each_distinct_rec[1],))
                    clas = self.cursor.fetchall()
                    c.setFont('Helvetica', 10)
                    
                    c.drawString(50, 260, 'To : %s class : %s'%(each_distinct_rec[0], clas[0][0]))
                    #Draw line to adm or id
                    c.setLineWidth(1)
                    c.line( 80, 255 , 90, 255)
                    #Draw line to class
                    c.setLineWidth(1)
                    c.line( 130, 255 , 170, 255)
                    #shows to who ?
                    c.setFont('Helvetica', 10)
                    c.drawString(50, 220, 'Served by : %s'%self.user_name)
        
                    c.showPage()
            
                    
                c.save()
                #clean the files for new pictures
                files = glob.glob('reports\\reports_images\\*')
                for f in files:
                    os.remove(f)
                    
                #generate pictures
                cpath = os.path.dirname(__file__)
                os.startfile('generate_reports.bat')
                
                content = MDLabel(font_style='Caption',text="reports generated successfully",\
                                  size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Reports generated",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
            else:
                content = MDLabel(font_style='Caption',text="No reports to generate",\
                                  size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="No reports",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
                
    def preview_reports(self):
        existing=[]
        for filename in glob.iglob('reports\\*.pdf'):
             existing.append(filename)
        #check if the generated barcode.pdf exists
        if 'reports\\report.pdf' not in existing:
            content = MDLabel(font_style='Caption',text="Generate report(s) first to proceed",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Nothing to print",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            #clean the files for new pictures
            files = glob.glob('reports\\reports_images\\*')
            
            
            if len(files)==0:
                self.img_preview.source='pics\\no_preview.png'
                self.lbl_preview.text='[b]Page(s): 0/%s[/b]'%len(files)
            else:
                #view pictures on the screen manager
                self.img_preview.source=files[0]
                self.img_preview.reload()
                self.lbl_preview.text='[b]Page(s): 1/%s[/b]'%len(files)
                
            self.index_preview=0
        
        
    ################################################################## BARCODE PRINTING AND GENERATING
    def revert_settings_preview(self):
        #set previous settings
        file=open('page_settings.txt','w')
        self.page_settings={'cols':4, 'rows':8, 'margin_x':10, 'margin_y':50, 'space_x':120, 'space_y':100, 'bar_width':0.5 , 'bar_height':20}
        file.write(str(self.page_settings))
        
        #revert values
        self.ids.margin_x.text = str(self.page_settings['margin_x'])
        self.ids.margin_y.text = str(self.page_settings['margin_y'])
        self.ids.nocpp.text = str(self.page_settings['cols'])
        self.ids.norpp.text = str(self.page_settings['rows'])
        self.ids.sbbx.text = str(self.page_settings['space_x'])
        self.ids.sbby.text = str(self.page_settings['space_y'])

        #save settings
        file=open('page_settings.txt','w')
        file.write(str(self.page_settings))
        content = MDLabel(font_style='Caption',text="Settings restored successfully",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Settings restored",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
        self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def set_settings_preview(self):
        self.page_settings['margin_x'] = self.ids.margin_x.text
        self.page_settings['margin_y'] =  self.ids.margin_y.text
        self.page_settings['cols'] = self.ids.nocpp.text
        self.page_settings['rows'] = self.ids.norpp.text
        self.page_settings['space_x'] = self.ids.sbbx.text
        self.page_settings['space_y'] = self.ids.sbby.text
        
        #save settings
        file=open('page_settings.txt','w')
        file.write(str(self.page_settings))
        content = MDLabel(font_style='Caption',text="Settings modified successfully",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Modification",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
        self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
        
        
    def move_preview_img(self,nop):
        existing=[]
        for filename in glob.iglob('barcode_file\\barcode_images\\*.png'):
             existing.append(filename)
        
        if nop=='n':
            if (self.index_preview+1) <= len(existing)-1:
                self.index_preview+=1
                self.ids.img_preview.source=existing[self.index_preview]
                self.ids.img_preview.reload()
                self.ids.lbl_preview.text='[b]Page(s): %s/%s[/b]'%(self.index_preview+1,len(existing))
        else:
            if (self.index_preview-1) >= 0:
                self.index_preview-=1
                self.ids.img_preview.source=existing[self.index_preview]
                self.ids.img_preview.reload()
                self.ids.lbl_preview.text='[b]Page(s): %s/%s[/b]'%(self.index_preview+1,len(existing))
        
    def preview_barcode(self):
        existing=[]
        for filename in glob.iglob('barcode_file\\*.pdf'):
             existing.append(filename)
        #check if the generated barcode.pdf exists
        if 'barcode_file\\barcode.pdf' not in existing:
            content = MDLabel(font_style='Caption',text="Generate a barcode first to proceed",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Nothing to print",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            #clean the files for new pictures
            files=[]
            for filename in glob.iglob('barcode_file\\barcode_images\\*'):
                 files.append(filename)

            if len(files)==0:
                self.ids.img_preview.source='pics\\no_preview.png'
                self.ids.lbl_preview.text='[b]Page(s): 0/%s[/b]'%len(files)
            else:
                #view pictures on the screen manager
                self.ids.img_preview.source=files[0]
                self.ids.img_preview.reload()
                self.ids.lbl_preview.text='[b]Page(s): 1/%s[/b]'%len(files)
                
            self.index_preview=0
   
    def print_file(self):
        existing=[]
        for filename in glob.iglob('barcode_file\\*.pdf'):
             existing.append(filename)

        #check if the generated barcode.pdf exists
        if 'barcode_file\\barcode.pdf' not in existing:
            content = MDLabel(font_style='Caption',text="Generate a barcode first to proceed",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Nothing to print",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            try:
                current =  os.getcwd()
                filename = 'barcode_file\\barcode.pdf'
                win32api.ShellExecute ( 0,"print",filename,
                 
                  '/c:"%s"' % win32print.GetDefaultPrinter (),
                  ".",
                  0
                )
            except:
                content = MDLabel(font_style='Caption',text="Ensure you have connected the printer you want to print with then proceed with printing",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Printer error !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()

    def generate_barcode(self,start,end):
        if start=='' or end=='':
            content = MDLabel(font_style='Caption',text="Enter a range to generate",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Nothing to generate",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            bar_code_start=int(start)
            bar_code_end=int(end)
            
            pages_total= (bar_code_end - bar_code_start)/ (int(self.page_settings['rows'])*int(self.page_settings['cols']))
            #check whether there is a decimal
            if isinstance(pages_total,float): 
                pages_total=int(pages_total)+1
            cpath = os.path.dirname(__file__)
            
            c=canvas.Canvas('barcode_file\\barcode.pdf',pagesize=A4)
            
            lbl_accession = bar_code_start
            for page in range(int(pages_total)):
                y= int(self.page_settings['margin_y'])
                
                for row in range(int(self.page_settings['rows'])):
                    
                    x = int(self.page_settings['margin_x'])
                    
                    for col in range(int(self.page_settings['cols'])):
                        
                        barcode=code39.Extended39( str(lbl_accession), barWidth= 0.5*mm, barHeight = 20*mm )
                        # drawOn puts the barcode on the canvas at the specified coordinates
                        barcode.drawOn(c, x, y)
                        c.drawString(x+60, y-20, str(lbl_accession))
                        x+= int(self.page_settings['space_x'])
                        lbl_accession+=1
                        
                    y+= int(self.page_settings['space_y'])
                c.showPage()

            c.save()
            #clean the files for new pictures
            files = glob.glob('barcode_file\\barcode_images\\*')
            for f in files:
                os.remove(f)
                
            #generate pictures
            import subprocess
            path = r'%s'%cpath
            #path1 =cpath +'\\barcode_file\\barcode.pdf'
            #path2 =cpath +'\\barcode_file\\barcode_images\\img.png'
            #print('main path='+cpath,'\npath1='+path1, '\npath2='+path2)
            #command = 'convert %s %s'%(path1,path2)
            
##            p = Popen(cpath+"\\generate.bat")
##            stdout, stderr = p.communicate()
            #DECLARE CONSTANTS
            DPI = 200
            THREAD_COUNT = 1
            USERPWD = None
            USE_CROPBOX = False
            STRICT = False
            pdf = PdfFileReader(open('barcode_file\\barcode.pdf','rb'))
            no_pages = pdf.getNumPages()
            pil_images = pdf2image.convert_from_path('barcode_file\\barcode.pdf',dpi=DPI, output_folder=None,\
                                                 first_page=1, last_page=no_pages, \
                                                 fmt='.png', thread_count=THREAD_COUNT,\
                                                 userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)

            c = 0
            for image in pil_images:
                image.save('barcode_file\\barcode_images\\'+ str(c) + ".png")
                c +=1
            
            #os.popen(cpath+'\\generate.bat')
            content = MDLabel(font_style='Caption',text="%s barcode generated"%int((bar_code_end)-(bar_code_start)),\
                              size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Barcode generated",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()        
        
    ################################################################## LODING PROFILE PIC
    def dismiss_popup(self):
        self._popup.dismiss()
        
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Pop(title="Load Profile picture", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        try:
            path_to='profile_pic\\%s'%self.user_name+'%s'%filename[0][-4:]
            self.prof_pic=filename[0]
            path_from=str(os.path.join(path, filename[0]))
            shutil.copyfile(path_from,path_to)
        except:
            pass
        
        self.dismiss_popup()
        
    ################################################################## SEARCH CRITERIA
    def specify_citeria(self, *args):
        for wid in self.dropdown.children[0].walk():
            if isinstance(wid, ToggleButton)==True:
                if wid.state=='down':
                    if wid.text !='Search by class':
                        self.criteria = wid.text
                    else:
                        self.criteria= "%s , %s(separated by a comma)"%(self.criteria,'Search by class')
                       
        self.ids.books_search.hint_text= self.criteria
        self.ids.books_search.text= ''
        
    #search according to the critria
    def search(self, criteria):
        criteria = self.criteria

        no_criteria = len(criteria.split(','))

        criteria = criteria.split(',')[0]
            
        what='title'
        print('criteria = ',criteria)
        if criteria=='Search book by title':
            what='title'
        elif criteria=='Search by Publisher':
            what='publisher'
        elif criteria=='Search by Author':
            what='author'
        elif criteria=='Search by Place of publication':
            what='place_of_publication'
        elif criteria=='Search by Year of publication':
            what='year_of_publication'
        elif criteria=='Search by category':
            what='category'
        elif criteria=='Search by book accession no.':
            what='book_accession_no'
        elif criteria=='Search by shelve no.':
            what='shelve_no'
        elif criteria=='Search by lost book':
            what='lost'
        elif criteria=='Search by borrowed book':
            what='borrowed'
        elif criteria=='Search by damaged book':
            what='damaged'
        elif criteria=='Search by Admission no':
            what='admission'

        if no_criteria==1:
            if what =='admission':
                self.cursor.execute('''SELECT * FROM books WHERE lost_by LIKE ? OR borrowed_by LIKE ? OR damaged_by LIKE ? ''',\
                                    ('%'+self.ids.books_search.text+'%', '%'+self.ids.books_search.text+'%', '%'+self.ids.books_search.text+'%',))
            else:
                self.cursor.execute('''SELECT * FROM books WHERE {} LIKE ? '''.format(what.replace('"','""')),('%'+self.ids.books_search.text+'%',))

            rec=self.cursor.fetchall()
        else:
            if what !='admission':
                contents = self.ids.books_search.text.split(',')
                rec = []
                if len(contents)==2:
                    #list all occurence of the books
                    self.cursor.execute('''SELECT * FROM books WHERE {}  LIKE ? '''.format(what.replace('"','""')),('%'+contents[0]+'%',))
                    books = self.cursor.fetchall()
                    print(books)

                    print(contents[1], 'stream')
                    #fetch all the students in the specific stream
                    self.cursor.execute('''SELECT adm_no FROM members WHERE class LIKE ? ''',('%s'+str(contents[1])+'%',))
                    members_adm = self.cursor.fetchall()
                    print(members_adm, 'members')
                    ne_m = []
                    for mem in members_adm:
                        ne_m.append( mem[0])
                        
                    #check if the member has borrowed the specific book
                    for book in books:
                        if book[14] in ne_m:
                            rec.append(book)
                    
        
        
        self.table_books.recv_add.data=[]

        wg = 'g'
        for row in rec:
            counter_column=0
            if wg == 'w':
                wg ='g'
            elif wg == 'g':
                wg = 'w'
            for cols in range(len(row)-1):
                self.table_books.recv_add.data.append({'text':str(row[counter_column]), 'wg':wg})
                counter_column+=1                
     
    ################################################################## DASHBOARD
    def refresh_total_no_books(self,*args):
        self.cursor.execute(''' SELECT count(*) FROM books''')
        total_no=self.cursor.fetchall()
        self.ids.dashlabel.text='{:,}'.format((total_no[0][0]))
        
    ################################################################## LOGIN        
    #log out confirmation
    def do_want_log_out(self):
        content = MDLabel(font_style='Caption',text="Are you sure you want to log out ?, this will enable you to switch users",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Log out",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",action=lambda *x: self.dialog.dismiss())
        self.dialog.add_action_button("Proceed",action=lambda *x: self.yeah_a_do())
        self.dialog.open()

    def reload_users(self):
        #Reading from registry 
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        aKey=OpenKey(aReg, r"SOFTWARE\LibrarySystem\accounts",0,KEY_ALL_ACCESS)
        value=QueryValueEx(aKey,'accounts')
        value=ast.literal_eval(value[0])

        self.ids.box_users.clear_widgets()
        
        for users in value.keys():
            wid = User_widet(username=users,\
                             password = value[users],\
                             pos_hint={'center_x':.5})
            wid.size = (dp(400), dp(150))
            self.ids.box_users.add_widget(wid)

            wid.ids.btn.bind(on_release=partial(self.permit_access, users, value[users],wid))
            wid.ids.txt.focus=True

    def yeah_a_do(self,*args):
        self.dialog.dismiss()
        #clear backup and notifications widgets
        self.ids.backup_grd.clear_widgets()
        self.ids.noti_grid_std.clear_widgets()
        self.ids.noti_grid_teach.clear_widgets()
        self.ids.noti_grid_non.clear_widgets()
        self.current='login'

    def populate_users(self):
        #Reading from registry 
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        aKey=OpenKey(aReg, r"SOFTWARE\LibrarySystem\accounts",0,KEY_ALL_ACCESS)
        value=QueryValueEx(aKey,'accounts')
        value=ast.literal_eval(value[0])

        for users in value.keys():
            wid = User_widet(username=users,\
                             password = value[users],\
                             pos_hint={'center_x':.5})
            wid.size = (dp(400), dp(150))
            self.ids.box_users.add_widget(wid)

            wid.ids.btn.bind(on_release=partial(self.permit_access, users, value[users], wid))
            wid.ids.txt.focus=True
            break
        
    def permit_access(self,username,passwd,wid, *args):
        #check for an empty field
        if wid.ids.txt.text =='' :
            content = MDLabel(font_style='Caption',text="Make sure you have filled every filled",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty fields !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
            
        else:
            if wid.ids.txt.text==passwd:
                self.user_name=str(username)
                self.current='main'
                wid.ids.txt.text=''
##                self.prof_pic='pic_control\\icon.ico'
##                files=[]
##                for (dirpath, dirnames, filenames) in os.walk('profile_pic\\.'):
##                    files.extend(filenames)
##                    break
##                if '%s.jpg'%self.user_name not in files:
##                    self.prof_pic='pic_control\\icon.ico'
            else:
                content = MDLabel(font_style='Caption',text="Wrong password try again !",\
                      size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Wrong Password",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
        
        
    #change password
    def change_password(self,old,new,conf):
        #Reading from registry 
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        aKey=OpenKey(aReg, r"SOFTWARE\LibrarySystem\accounts",0,KEY_ALL_ACCESS)
        value=QueryValueEx(aKey,'accounts')
        value=ast.literal_eval(value[0]) #current password
        current_user_pass=value[self.user_name]
      
        if current_user_pass !=old:
            content = MDLabel(font_style='Caption',text="Current password is wrong",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Password mismatch !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            if new != conf:
                content = MDLabel(font_style='Caption',text="New password dont match the confrimation password",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Password mismatch !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()

            else:
                if new == '' or conf =='':
                    content = MDLabel(font_style='Caption',text="Password cannot be empty",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
                    content.bind(texture_size=content.setter('size'))
                    self.dialog = MDDialog(title="Empty fields !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                    self.dialog.open()
                else:
                    #change password
                    value[self.user_name]=conf
                    Key = CreateKeyEx(aReg, r"SOFTWARE\LibrarySystem\accounts", 0, KEY_ALL_ACCESS) 
                    SetValueEx(aKey,"accounts",0, REG_SZ, str(value)) 
                    CloseKey(aKey)

                    content = MDLabel(font_style='Caption',text="Password is changed successfully",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
                    content.bind(texture_size=content.setter('size'))
                    self.dialog = MDDialog(title="Password !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                    self.dialog.open()

    #create new account
    def create_new_account(self,username,passwd,conf):
        
        if username=='' or passwd=='' or conf=='':
            content = MDLabel(font_style='Caption',text="Ensure you have filled every fields",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty fields !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            if passwd != conf:
                content = MDLabel(font_style='Caption',text="Password dont match !",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Password mismatch !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
            else:
                if self.user_name !='Administrator':
                    content = MDLabel(font_style='Caption',text="You must be an Administrator to create an account",\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
                    content.bind(texture_size=content.setter('size'))
                    self.dialog = MDDialog(title="No permissions  !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                    self.dialog.open()
                else:
                    
                    #Reading from registry 
                    aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
                    aKey=OpenKey(aReg, r"SOFTWARE\LibrarySystem\accounts",0,KEY_ALL_ACCESS)
                    value=QueryValueEx(aKey,'accounts')
                    value=ast.literal_eval(value[0]) #current dictionary

                    # add the account
                    value[username]=conf
                    #write to registry account
                    Key = CreateKeyEx(aReg, r"SOFTWARE\LibrarySystem\accounts", 0, KEY_ALL_ACCESS) 
                    SetValueEx(aKey,"accounts",0, REG_SZ, str(value)) 
                    CloseKey(aKey)
                    
                    content = MDLabel(font_style='Caption',text="New account created successfully !",\
                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                    content.bind(texture_size=content.setter('size'))
                    self.dialog = MDDialog(title="Account created !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
                    self.dialog.open()
                
                
        
    
    ################################################################## ANALYSIS
    def estimate_book_quantity(self):
        #fetch a book uniquely
        self.cursor.execute('''SELECT DISTINCT title FROM books ''')
        rec=self.cursor.fetchall()
        self.ids.rvanlysis.data=[]
        for each_rec in rec:
            self.ids.rvanlysis.data.append({'text':str(each_rec[0])})

    def search_analysis_books(self,txt):
        #search for the books
        txts = '%'+txt+'%'
        self.cursor.execute(''' SELECT DISTINCT title FROM books WHERE title LIKE ? ''',(txts,))
        rec = self.cursor.fetchall()

        self.ids.rvanlysis.data=[]
        for each_rec in rec:
            self.ids.rvanlysis.data.append({'text':str(each_rec[0])})
            
    # show analysis of a book and graph
    def show_book_quantity(self, value):
        #count the number of the value books
        self.cursor.execute(''' SELECT count(*) FROM books WHERE title= ? ''',(value,))
        book_no=self.cursor.fetchall()
        #count the total number of the books
        self.cursor.execute(''' SELECT count(*) FROM books  ''')
        total_book_no=self.cursor.fetchall()
        book_no=book_no[0][0]
        total_book_no=total_book_no[0][0]
        
        self.ids.lbl_analysis0.text='''The number of %s is %s out of %s. The total number of books in the database is %s'''\
                                                                                        %(value, book_no, (total_book_no-book_no), total_book_no)
        self.ids.lbl_title0.text='''[u]{} Analysis [/u]'''.format(value)

        labels= value,'Rest of the books'
        sizes=[book_no,total_book_no-book_no]
        colors=['gold','lightskyblue']
        explode=(None) #explode a sclice if required

        plt.pie(sizes, explode=explode, labels=labels ,colors=colors, autopct='%1.1f%%', shadow=False)
        
        #draw a circle at the center to make it look loke a donut
        center_circle=plt.Circle((0,0),0.75,color='white',fc='white',linewidth=1.25)
        fig=plt.gcf()
        fig.gca().add_artist(center_circle)

        #set aspect ratio to be equal so that pie is drawn as a circle
        plt.axis('equal')
        plt.savefig('graph.png')
        plt.close(fig)
        
        self.ids.graph_plot0.source='graph.png'
        self.ids.graph_plot0.reload()

        #propotion of books borrowed
        self.cursor.execute(''' SELECT book_accession_no FROM books WHERE borrowed='yes' ''')
        borrowed_books_accession_no=self.cursor.fetchall()
        
        std_no=0
        teach=0
        non=0
        
        #calc the number of the book borrowed
        for each_acc in borrowed_books_accession_no:
            self.cursor.execute('''SELECT member_type FROM borrow WHERE book_accession_no=? ''',(each_acc[0],))
            mem_typ=self.cursor.fetchall()
            if mem_typ[0][0]=='student':
                self.cursor.execute(''' SELECT title FROM books WHERE book_accession_no= ? ''',(each_acc[0],))
                book_tit=self.cursor.fetchall()
                if book_tit[0][0]==value:
                    std_no+=1
            elif mem_typ[0][0]=='teacher':
                self.cursor.execute(''' SELECT title FROM books WHERE book_accession_no= ? ''',(each_acc[0],))
                book_tit=self.cursor.fetchall()
                if book_tit[0][0]==value:
                    teach+=1
            else:
                self.cursor.execute(''' SELECT title FROM books WHERE book_accession_no= ? ''',(each_acc[0],))
                book_tit=self.cursor.fetchall()
                if book_tit[0][0]==value:
                    non+=1
                  
        rem_books=book_no -(std_no + teach + non)
        
        self.ids.lbl_title1.text='''[u]Proportion of how {} is borrowed[/u]'''.format(value)
        self.ids.lbl_analysis1.text='%s %s has been borrowed by students, %s %s has been borrowed by teachers, %s %s has been borrowed by non teaching stuff.Books left is %s.'%(std_no,value,teach,value,non,value,rem_books)
        
        #graph for proportions
        labels= 'students','teachers','non teaching...','not borrowed'
        sizes=[std_no, teach, non, rem_books]
        colors=['gold','lightskyblue','lightcoral',[0,0,0,.3]]
        explode=(None) #explode a sclice if required

        plt.pie(sizes, explode=explode, labels=labels ,colors=colors, autopct='%1.1f%%', shadow=False)
        
        #draw a circle at the center to make it look loke a donut
        center_circle=plt.Circle((0,0),0.75,color='white',fc='white',linewidth=1.25)
        fig=plt.gcf()
        fig.gca().add_artist(center_circle)

        #set aspect ratio to be equal so that pie is drawn as a circle
        plt.axis('equal')
        plt.savefig('graph1.png')
        plt.close(fig)
    
        self.ids.graph_plot1.source='graph1.png'
        self.ids.graph_plot1.reload()

  
        
    ################################################################## BARCODES
        
    ################################################################## BACKUP
    #add database buttons
    def add_backup_buttons(self,*args):
        #list the backup
        backup_list=os.listdir('backups')
        backup_list1=[x.split('.db')[0] for x in backup_list]
        backup_list1=sorted(backup_list1)
        backup_list1.reverse()
        self.ids.backup_grd.clear_widgets()
        for content in backup_list1:
            self.backupButton=Backup_restore(size_hint=(1,None),size=(1,60))
            self.backupButton.ids.mdl.text=content.replace('.',':')
            self.backupButton.ids.btn.bind(on_release=partial(self.replace_the_database,content))
            threading.Thread(target=self.add_backup_button1,args=(content,)).start()
            
    def add_backup_button1(self,bk,*args):
        self.ids.backup_grd.add_widget(self.backupButton)
            
    def replace_the_database(self,file,*args):
        content = MDLabel(font_style='Caption',text="Are you sure you want to replace the current database with the %s backed up one ?"%file,\
                          size_hint=(1,None),valign='middle',halign='left',markup=True)
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Warning ",content=content,size_hint=(.4, None),height=(200),auto_dismiss=False)
        self.dialog.add_action_button("yes",action=lambda *x: self.do_replace(file))
        self.dialog.add_action_button("no",action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    #replace the current database with the backuped one
    def do_replace(self,file,*args):
        self.dialog.dismiss()
        #replace
        self.connection.close()
        shutil.copyfile('backups\\%s.db'%file,'database.db')
        self.connection = sqlite3.connect('file:database.db?mode=rw', uri=True)
        self.cursor=self.connection.cursor()
        
        self.show_notification('Database replaced successfully',10)

        #clean ui to rub out errors
        self.table_books.data = []
        self.Gridlayout_non_issue.clear_widgets()
        self.Gridlayout_non_history.clear_widgets()
        self.Gridlayout_teach_history.clear_widgets()
        self.Gridlayout_teach_issue.clear_widgets()
        self.Gridlayout_std_history.clear_widgets()
        self.Gridlayout_std_issue.clear_widgets()
        
        self.ids.noti_grid_std.clear_widgets()
        self.ids.rvanlysis.data=[]
        
    #check for a backup
    def do_backup(self,*args):
        #check if the backup counter is exceed the limits
        if self.backup_counter >= 20:
            # create a backup
            if os.path.isdir("backups")==True:
                now=datetime.datetime.now()
                now_fmt=now.strftime("%Y-%m-%d %H.%M.%S")
                shutil.copyfile('database.db','backups\\%s.db'% now_fmt)
                self.show_notification('A new backup for the database is created ',5)
            self.backup_counter=0
            #save the backup_counter
            a=open('backup_counter.txt','w')

            a.write(str(self.backup_counter))
            a.close()
            
    #manual backup
    def backup_manaully(self):
        # create a backup
        if os.path.isdir("backups")==True:
            now=datetime.datetime.now()
            now_fmt=now.strftime("%Y-%m-%d %H.%M.%S")
            shutil.copyfile('database.db','backups\\%s.db'% now_fmt)
            self.show_notification('A new backup for the database is created ',5)

    #exteranl backup of the database
    def show_save(self):
        content = SaveDialog(save=self.backup_external, cancel=self.dismiss_popup)
        self._popup = Pop(title="Save database to an external location", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
        
    def backup_external(self, path, filename):
        db_path=os.getcwd()+'\\'+'database.db'
        to_path=path+'\\'+filename+'.db'
        shutil.copyfile(db_path,to_path)

        self._popup.dismiss()
    ################################################################## AUTO FILL FEATURE
    def auto_complete_feature(self, navtools, *args):
        if self.autocomplete ==True:
            if len(navtools['tit'].text) > 1:
                #create a dropdown
                self.dropdown_autocomplete = CustomDropdown()
                self.dropdown_autocomplete.dismiss_on_select=True

                connection = sqlite3.connect('file:%s?mode=rw'%("autocomplete\\new.db"), uri=True)
                cursor=connection.cursor()
                #query for the search and retreive the results
                txts= "%"+navtools['tit'].text+"%"
                results = []
                cursor.execute(''' SELECT DISTINCT isbn, title, publisher, edition, author, place_of_publication, year_of_publication FROM books WHERE title LIKE ?''',(txts,))
                results = cursor.fetchall()

                #show the results in a dropdown button if there is record to show
                for res in results:
                    btn = AutocompleteButton(isbn=res[0],\
                                             title=res[1],\
                                             publisher=res[2],\
                                             edition=res[3],\
                                             author=res[4],\
                                             place_of_publication=res[5],\
                                             year_of_publication=res[6],\
                                             text = res[1],\
                                             size_hint_x=1,\
                                             width= navtools['tit'].width,
                                             pos_hint={'center_x':.5})
                    
                    self.dropdown_autocomplete.add_widget(btn)
                        
                    btn.bind(on_press=partial(self.fill_autocomplete_suggestion, btn, navtools))

                if len(self.dropdown_autocomplete.children)>0:
                    self.dropdown_autocomplete.open(navtools['tit'])

    def fill_autocomplete_suggestion(self, btn,navtools,*args):
        navtools['isbn'].text = btn.isbn
        navtools['tit'].text = btn.title
        navtools['pubr'].text = btn.publisher
        navtools['edition'].text = btn.edition
        navtools['auth'].text = btn.author
        navtools['pob'].text = btn.place_of_publication
        navtools['yop'].text = btn.year_of_publication
        self.dropdown_autocomplete.dismiss()
        
    
        
    ################################################################## NOTIFICATIONS
    #add notifications widgets
    def show_noti_widgets(self):
        #regresh the database content
        self.timer_start_work_notification()
        
        self.cursor.execute(''' SELECT date_passed_by, member_type, id_no, adm_no, book_accession_no FROM borrow ORDER BY date_passed_by ASC''')
        noti_rec_total=self.cursor.fetchall()
        self.ids.noti_grid_std.clear_widgets()
        self.ids.noti_grid_teach.clear_widgets()
        self.ids.noti_grid_non.clear_widgets()
        
        #calculate the total notifications ,students,teachers & non teaching stuff
        for rec in noti_rec_total:
            #get book name
            self.cursor.execute(''' SELECT title FROM books WHERE book_accession_no=? ''',(rec[4],))
            book_name=self.cursor.fetchall()
            
            #students
            if rec[0].find('-')==-1 and int(rec[0]) > 0 and rec[1]=='student':
                #get students name
                self.cursor.execute(''' SELECT name FROM members WHERE adm_no=? ''',(rec[3],))
                std_name=self.cursor.fetchall()
                self.noti_btn_std=NotificationB(rec[3],std_name[0][0],book_name[0][0],rec[1],rec[0],size_hint=(1,None),size=(1,130))
                self.noti_btn_std.ids.adm_id_lbl.text='Admission no. :'
                self.noti_btn_std.ids.show_mem.bind(on_release=partial(self.direct_to_where,rec[1],self.noti_btn_std))
                threading.Thread(target=self.notification_buttons,args=(rec[1],)).start()
            #teachers
            if rec[0].find('-')==-1 and int(rec[0]) != 0 and rec[1]=='teacher':
                #get teachers name
                self.cursor.execute(''' SELECT name FROM members WHERE id_no=? ''',(rec[2],))
                teach_name=self.cursor.fetchall()
                self.noti_btn_teach=NotificationB(rec[2],teach_name[0][0],book_name[0][0],rec[1],rec[0],size_hint=(1,None),size=(1,130))
                self.noti_btn_teach.ids.adm_id_lbl.text='Id no. :'
                self.noti_btn_teach.ids.show_mem.bind(on_release=partial(self.direct_to_where,rec[1],self.noti_btn_teach))
                threading.Thread(target=self.notification_buttons,args=(rec[1],)).start()
            #non teachers
            if rec[0].find('-')==-1 and int(rec[0]) != 0 and rec[1]=='non':
                #get non teaching stuff name
                self.cursor.execute(''' SELECT name FROM members WHERE id_no=? ''',(rec[2],))
                non_name=self.cursor.fetchall()
                self.noti_btn_non=NotificationB(rec[2],non_name[0][0],book_name[0][0],rec[1],rec[0],size_hint=(1,None),size=(1,130))
                self.noti_btn_non.ids.adm_id_lbl.text='Id no. :'
                self.noti_btn_non.ids.show_mem.bind(on_release=partial(self.direct_to_where,rec[1],self.noti_btn_non))
                threading.Thread(target=self.notification_buttons,args=(rec[1],)).start()

    def direct_to_where(self,member_type,inst, *args):
        if member_type=='student':
            self.wid_std_circ_scrolls['adm_no'].text=inst.ids.adm_id.text
            self.std_search_circ_for_std(self.txt_remarks)
            self.ids.sm_content.current='Students_borro_ret'
            self.ids.sm_title.current='Students_borro_ret'
        elif member_type=='teacher':
            self.wid_teach_circ_scrolls['id_no'].text= inst.ids.adm_id.text
            self.teach_search_circ(self.txt_remarks_teach)
            self.ids.sm_content.current='Teachers_borro_ret'
            self.ids.sm_title.current='Teachers_borro_ret'
        else:
            self.wid_non_circ_scrolls['id_no'].text= inst.ids.adm_id.text
            self.non_search_circ(self.txt_remarks_non)
            self.ids.sm_content.current='non_teaching_borro_ret'
            self.ids.sm_title.current='non_teaching_borro_ret'
            
                
    def notification_buttons(self,member_type, *args):
        if member_type=='student':
            self.ids.noti_grid_std.add_widget(self.noti_btn_std)
        elif member_type=='teacher':
            self.ids.noti_grid_teach.add_widget(self.noti_btn_teach)
        else:
            self.ids.noti_grid_non.add_widget(self.noti_btn_non)
    
    def change_cards(self,*args):
        self.ids.smn_dash.index=secrets.choice(self.screen_list)
    
    def update_cards_content(self,*args):
        self.cursor.execute(''' SELECT date_passed_by, member_type FROM borrow''')
        noti_rec_total=self.cursor.fetchall()

        #calculate the total notifications ,students,teachers & non teaching stuff
        totl_counter=0
        std_counter=0
        teach_counter=0
        non_counter=0
        for rec in noti_rec_total:
            #total
            if rec[0].find('-')==-1 and int(rec[0]) > 0:
                totl_counter+=1
            #students
            if rec[0].find('-')==-1 and int(rec[0]) > 0 and rec[1]=='student':
                std_counter+=1
            #teachers
            if rec[0].find('-')==-1 and int(rec[0]) > 0 and rec[1]=='teacher':
                teach_counter+=1
            #non teachers
            if rec[0].find('-')==-1 and int(rec[0]) > 0 and rec[1]=='non':
                non_counter+=1
                
        self.ids.smn_dash.ids.not_total.text = str(totl_counter)+' total notifications'
        self.ids.smn_dash.ids.not_std.text = str(std_counter)+' books should be returned by students'
        self.ids.smn_dash.ids.not_teach.text = str(teach_counter)+' books should be returned by teachers'
        self.ids.smn_dash.ids.not_non.text =str( non_counter)+' books should be returned by non teaching stuff'

    def timer_start_work_notification(self,*args):
        #fetch the data for manupulation
        self.cursor.execute(''' SELECT adm_no, id_no, date_suppossed_return, member_type, book_accession_no FROM borrow''')
        rec_calc=self.cursor.fetchall()
        self.notification_group=[] #for keeping all the notifications
        #manupulate each record by finding the date passed (now-date_suppossed_return)
        for eachr in rec_calc:
            adm_no=eachr[0]
            id_no=eachr[1]
            date_suppossed_return=eachr[2]
            member_type=eachr[3]
            #subtract now-date_suppossed_return
            today_date=str(datetime.datetime.now())[:10]
            today_day=today_date[8:10]
            today_month=today_date[5:7]
            today_year=today_date[:4]

            #check for errors
            dt=datetime.datetime.strptime(date_suppossed_return,'%d/%m/%Y')
            return_day=dt.day
            return_month=dt.month
            return_year=dt.year

            #set format for the dates
            tod_date = datetime.date(int(today_year), int(today_month), int(today_day))
            supp_ret_date = datetime.date(int(return_year), int(return_month), int(return_day))
            
            #subtract the dates
            date_diff=tod_date-supp_ret_date
            rem_days=str(date_diff.days)
            
            #append to a record 
            rec_one=[adm_no, id_no, rem_days, member_type,eachr[4]]
            self.notification_group.append(rec_one)

            
        #update the borrow table
        for eachr in self.notification_group:
            if eachr[3]=='student':
                if eachr[2][0]=='-':
                    eachr[2]=0
                self.cursor.execute(''' UPDATE borrow SET date_passed_by=? WHERE adm_no=? AND book_accession_no =? ''',(eachr[2], eachr[0], eachr[4],))
            else:
                if eachr[2][0]=='-':
                    eachr[2]=0
                self.cursor.execute(''' UPDATE borrow SET date_passed_by=? WHERE id_no=? AND book_accession_no =? ''',(eachr[2], eachr[1], eachr[4],))
            self.connection.commit()
            
            
    ############################################### BOOKS CIRCULATION
    #searches for borrowed and history books
    def do_search_for_records_circ(self,scrolls, txtw, gridl, gridh, soo, brohs,*args):
        #check if its borrow or history
        if brohs=='br':
            #refresh the database first
            self.timer_start_work_notification()

            if soo=='s':
                self.cursor.execute(''' SELECT book_accession_no, date_issued, date_suppossed_return, date_passed_by, adm_no, id_no,\
                                                            by_user  FROM borrow WHERE book_accession_no=? AND adm_no=? ''',(txtw.text, scrolls['adm_no'].text,))
            else:
                self.cursor.execute(''' SELECT book_accession_no, date_issued, date_suppossed_return, date_passed_by, adm_no, id_no,\
                                                            by_user  FROM borrow WHERE book_accession_no=? AND id_no=? ''',(txtw.text, scrolls['id_no'].text,))
                
            book_acc_no=self.cursor.fetchall()

            gridl.clear_widgets()
            for books in book_acc_no:
                self.cursor.execute(''' SELECT title, publisher,lost FROM books WHERE book_accession_no=?''',(txtw.text,))
                det=self.cursor.fetchall()
                    
                #check if book is lost
                if det[0][2]=='yes':
                    if soo=='s':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'student', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='student'
                        self.BorrowB.ids.pers.text='Admission no. :'
                        self.BorrowB.ids.adm_id.text=books[4]
                    elif soo=='t':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'teacher', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='teacher'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    else:
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'Non teaching stuff', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='Non teaching stuff'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    self.BorrowB.ids.imgb.source='pics\\book_lost.png'
                    self.BorrowB.ids.marklost.text='Mark book as not lost'
                    threading.Thread(target=self.show_current_borrowed_books,args=(self.BorrowB,gridl,)).start()
                else:
                    if soo=='s':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'student', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='student'
                        self.BorrowB.ids.pers.text='Admission no. :'
                        self.BorrowB.ids.adm_id.text=books[4]
                    elif soo=='t':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'teacher', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='teacher'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    else:
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'Non teaching stuff', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='Non teaching stuff'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    self.BorrowB.ids.imgb.source='pics\\book.png'
                    threading.Thread(target=self.show_current_borrowed_books,args=(self.BorrowB,gridl,)).start()
        else:
            #fetch everything from table history
            if soo=='s':
                self.cursor.execute(''' SELECT * FROM history WHERE adm_no=? AND book_accession_no=? ''',(scrolls['adm_no'].text, txtw.text,))
            else:
                self.cursor.execute(''' SELECT * FROM history WHERE id_no=? AND book_accession_no=? ''',(scrolls['id_no'].text, txtw.text,))
            hist_rec=self.cursor.fetchall()
            gridh.clear_widgets()
            for rec in hist_rec:
                #fetch books details from table books
                self.cursor.execute(''' SELECT title, publisher FROM books WHERE book_accession_no=? ''',(rec[1],))
                rec_bd=self.cursor.fetchall()
                Histotyb=HistoryButton(rec[1], rec_bd[0][0], rec_bd[0][1], rec[4], rec[5], rec[6], rec[7], size_hint=(1,None),size=(1,100))
                Histotyb.ids.imgb.source='pics\\book_history.png'
                threading.Thread(target=self.load_histry_buttons,args=(gridh,Histotyb,)).start()
                
    
    def to_deactivate_member(self,scrolls,soo,de_re='deactivate',*args):
        if soo=='s':
            adm_id=scrolls['adm_no'].text
        else:
            adm_id=scrolls['id_no'].text

        #display dialog for either activate or deactivate
        if de_re=='deactivate':
            content = MDLabel(font_style='Caption',text=" Are you sure you want to deactivate %s "%adm_id, size_hint=(1,None),valign='middle',halign='left',markup=True)
        else:
            content = MDLabel(font_style='Caption',text=" Are you sure you want to activate %s "%adm_id, size_hint=(1,None),valign='middle',halign='left',markup=True)
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Confirm",content=content,size_hint=(.4, None),height=(200),auto_dismiss=False)
        self.dialog.add_action_button("No",action=lambda *x: self.dialog.dismiss())
        self.dialog.add_action_button("Yes",action=lambda *x: self.confrim_deactivate_act(scrolls, soo, de_re))
        self.dialog.open()
            
                
    def confrim_deactivate_act(self,scrolls,soo,de_re='deactivate'):
        self.dialog.dismiss()
        self.deactivate_re_member(scrolls, soo, de_re)
        
        
    def deactivate_re_member(self, scrolls,soo,de_re='deactivate'):
        #check if the scroll is empty
        continu=False
        if soo=='s':
            if scrolls['adm_no'].text=='':
                content = MDLabel(font_style='Caption',text=" Enter an admission number to deactivate the member ", size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Empty Admission number !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                self.dialog.open()
            else:
                continu=True
        elif soo=='t' or soo=='n':
            if scrolls['id_no'].text=='':
                content = MDLabel(font_style='Caption',text=" Enter an Id number to deactivate the member ", size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Empty Admission number !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                self.dialog.open()
            else:
                continu=True
                
        #check if the record exists
        exists=False
        if continu==True:
            if soo=='s':
                self.cursor.execute(''' SELECT name FROM members WHERE adm_no =? ''',(scrolls['adm_no'].text,))
                rec_no=self.cursor.fetchall()
                if len(rec_no)>0:
                    exists=True
                else:
                    content = MDLabel(font_style='Caption',text=" Sorry this member doesn't exists", size_hint=(1,None),valign='middle',halign='left',markup=True)
                    content.bind(texture_size=content.setter('size'))
                    self.dialog = MDDialog(title="Member not found !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                    self.dialog.open()
            else:
                self.cursor.execute(''' SELECT name FROM members WHERE id_no =? ''',(scrolls['id_no'].text,))
                rec_no=self.cursor.fetchall()
                if len(rec_no)>0:
                    exists=True
                else:
                    content = MDLabel(font_style='Caption',text=" Sorry this member doesn't exists", size_hint=(1,None),valign='middle',halign='left',markup=True)
                    content.bind(texture_size=content.setter('size'))
                    self.dialog = MDDialog(title="Member not found !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                    self.dialog.open()
                    
        #if record exists proceed with updating the (deactivate and date deactivate)
        if exists==True:
            if soo=='s':
                #check if it is to activate or deactivate
                if de_re=='deactivate':
                    #update the rec
                    today_date=str(datetime.datetime.now())[:10]
                    self.cursor.execute(''' UPDATE members SET deactivate = 'yes', date_deactivate =? WHERE adm_no=? ''',(today_date,scrolls['adm_no'].text,))
                    self.connection.commit()
                    #change the colors    
                    self.mark_the_padlocks(scrolls,'s')
                else:
                    #update the rec
                    self.cursor.execute(''' UPDATE members SET deactivate = 'no', date_deactivate ="" WHERE adm_no=? ''',(scrolls['adm_no'].text,))
                    self.connection.commit()
                    #change the colors    
                    self.mark_the_padlocks(scrolls,'s')
            else:
                 #check if it is to activate or deactivate
                if de_re=='deactivate':
                    #update the rec
                    today_date=str(datetime.datetime.now())[:10]
                    self.cursor.execute(''' UPDATE members SET deactivate = 'yes', date_deactivate =? WHERE id_no=? ''',(today_date,scrolls['id_no'].text,))
                    self.connection.commit()
                    if soo=='t':
                        #change the colors    
                        self.mark_the_padlocks(scrolls,'t')
                    else:
                        #change the colors    
                        self.mark_the_padlocks(scrolls,'n')
                else:
                    #update the rec
                    self.cursor.execute(''' UPDATE members SET deactivate = 'no', date_deactivate ="" WHERE id_no=? ''',(scrolls['id_no'].text,))
                    self.connection.commit()
                    if soo=='t':
                        #change the colors    
                        self.mark_the_padlocks(scrolls,'t')
                    else:
                        #change the colors    
                        self.mark_the_padlocks(scrolls,'n')
                    
    #update remarks
    def update_remarks(self,scrolls,soo,*args):
        if soo=='s':
            self.cursor.execute('''UPDATE members  SET remarks =? WHERE adm_no=? ''',(self.txt_remarks.text,scrolls['adm_no'].text,))
            self.connection.commit()
        elif soo=='t':
            self.cursor.execute('''UPDATE members  SET remarks =? WHERE id_no=? ''',(self.txt_remarks_teach.text,scrolls['id_no'].text,))
            self.connection.commit()
        else:
            self.cursor.execute('''UPDATE members  SET remarks =? WHERE id_no=? ''',(self.txt_remarks_non.text,scrolls['id_no'].text,))
            self.connection.commit()
                             
                             
    
    #for non Teaching stuff search
    def book_search_circ_for_non(self,*args):
        #check for book existance
        acc_n=self.wid_non_circ_scrolls['book_acc_no'].text
        self.cursor.execute(''' SELECT * FROM books WHERE book_accession_no=? ''',(acc_n,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)

        controls=self.wid_non_circ_scrolls
        if rec_no!=0:
            recs=rec[rec_no-1]
            controls['titl'].text=str(recs[3])
            controls['pub'].text=str(recs[4])

            if self.ids.apply_b_i.active==True:
                self.combined_circ_add_rec(self.wid_non_circ_scrolls, self.nav_non_teaching_issue,\
                                                               self.wid_non_circ_input, 'n')
        else:
            controls['book_acc_no'].text='No such book in the database !'
            controls['titl'].text=''
            controls['pub'].text=''
            
    def non_search_circ(self,remark,*args):
        #check if member is registered
        id_no=self.wid_non_circ_scrolls['id_no'].text
        self.cursor.execute(''' SELECT * FROM members WHERE id_no =? AND member_type='non_teacher' ''',(id_no,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)

        scrolls=self.wid_non_circ_scrolls
        if rec_no!=0:
            recs=rec[rec_no-1]
            scrolls['id_no'].text=str(recs[3])
            scrolls['name'].text=str(recs[4])
            remark.text=str(recs[6])
            #load image
            req_pic='%s.jpg'%self.wid_non_circ_scrolls['id_no'].text
            
            if req_pic not in self.teach_pics:
                self.img_non_teaching_issue.img.source='pics\\account.png'
            else:
                self.img_non_teaching_issue.img.reload()
                self.img_non_teaching_issue.img.source='non_pics\\%s.jpg'%self.wid_non_circ_scrolls['id_no'].text

            #load borrowed books
            self.show_current_books(scrolls,self.Gridlayout_non_issue,self.current_non_issue,'n')
            #load history controls
            self.load_history_book(scrolls, self.Gridlayout_non_history, self.history_non_issue,'n')
            #change the colors    
            self.mark_the_padlocks(scrolls,'n')

            if self.ids.apply_b_i.active==True:
                scrolls['book_acc_no'].focus=True
            
        else:
            #if no record found
            scrolls['id_no'].text='No such non teaching stuff record in database !'
            scrolls['name'].text=''
            self.current_non_issue.ids.lbltitle.text=' Current borrowed books '
            self.history_non_issue.ids.lbltitle.text=' History of books '
        
    #for Teachers search
    def book_search_circ_for_teach(self,*args):
        #check for book existance
        acc_n=self.wid_teach_circ_scrolls['book_acc_no'].text
        self.cursor.execute(''' SELECT * FROM books WHERE book_accession_no=? ''',(acc_n,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)

        controls=self.wid_teach_circ_scrolls
        if rec_no!=0:
            recs=rec[rec_no-1]
            controls['titl'].text=str(recs[3])
            controls['pub'].text=str(recs[4])

            if self.ids.apply_b_i.active==True:
                self.combined_circ_add_rec( self.wid_teach_circ_scrolls, self.nav_teachers_issue,\
                                                               self.wid_teach_circ_input, 't')
            
        else:
            controls['book_acc_no'].text='No such book in the database !'
            controls['titl'].text=''
            controls['pub'].text=''
            
    def teach_search_circ(self,remark,*args):
        #check if member is registered
        id_no=self.wid_teach_circ_scrolls['id_no'].text
        self.cursor.execute(''' SELECT * FROM members WHERE id_no =? AND member_type='teacher' ''',(id_no,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)
        
        scrolls=self.wid_teach_circ_scrolls
        if rec_no!=0:
            recs=rec[rec_no-1]
            scrolls['id_no'].text=str(recs[3])
            scrolls['name'].text=str(recs[4])
            remark.text=str(recs[6])
            #load image
            req_pic='%s.jpg'%self.wid_teach_circ_scrolls['id_no'].text
            
            if req_pic not in self.teach_pics:
                self.img_teachers_issue.img.source='pics\\account.png'
            else:
                self.img_teachers_issue.img.reload()
                self.img_teachers_issue.img.source='teach_pic\\%s.jpg'%self.wid_teach_circ_scrolls['id_no'].text
            
            #load borrowed books
            self.show_current_books(scrolls,self.Gridlayout_teach_issue,self.current_Teachers_issue,'t')
            #load history controls
            self.load_history_book(scrolls, self.Gridlayout_teach_history, self.history_teach_issue,'t')
            #change the colors    
            self.mark_the_padlocks(scrolls,'t')

            if self.ids.apply_b_i.active==True:
                scrolls['book_acc_no'].focus=True
        else:
            #if no record found
            scrolls['id_no'].text='No such teachers in database !'
            scrolls['name'].text=''
            self.current_Teachers_issue.ids.lbltitle.text=' Current borrowed books '
            self.history_teach_issue.ids.lbltitle.text=' History of books '
    
    #for students search
    def book_search_circ_for_std(self,*args):
        #check for book existance
        acc_n=self.wid_std_circ_scrolls['book_acc_no'].text
        self.cursor.execute(''' SELECT * FROM books WHERE book_accession_no=? ''',(acc_n,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)

        controls=self.wid_std_circ_scrolls
        if rec_no!=0:
            recs=rec[rec_no-1]
            controls['titl'].text=str(recs[3])
            controls['pub'].text=str(recs[4])
        else:
            controls['book_acc_no'].text='No such book in the database !'
            controls['titl'].text=''
            controls['pub'].text=''

        if self.ids.apply_b_i.active==True:
            self.combined_circ_add_rec(self.wid_std_circ_scrolls, self.nav_std_issue, self.wid_std_circ_input,'s')
        
            
    def std_search_circ_for_std(self,remarks,*args):
        #check if member is registered
        adm=self.wid_std_circ_scrolls['adm_no'].text
        self.cursor.execute(''' SELECT * FROM members WHERE adm_no =? ''',(adm,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)

        scrolls=self.wid_std_circ_scrolls
        if rec_no!=0:
            recs=rec[rec_no-1]
            scrolls['clas'].text=str(recs[2])
            scrolls['id_no'].text=str(recs[3])
            scrolls['name'].text=str(recs[4])
            remarks.text=str(recs[6])
            #load image
            req_pic='%s.jpg'%self.wid_std_circ_scrolls['adm_no'].text
            
            if req_pic not in self.std_pics:
                self.img_std_issue.img.source='pics\\account.png'
            else:
                
                self.img_std_issue.ids.img.source='std_pic\\%s.jpg'%self.wid_std_circ_scrolls['adm_no'].text
                self.img_std_issue.ids.img.reload()
               
            #load borrowed books
            self.show_current_books(scrolls,self.Gridlayout_std_issue,self.current_std_issue,'s')
            #load history
            self.load_history_book(scrolls, self.Gridlayout_std_history, self.history_std_issue,'s')
            #change the colors    
            self.mark_the_padlocks(scrolls,'s')

            if self.ids.apply_b_i.active==True:
                scrolls['book_acc_no'].focus=True
            
        else:
            #if no record found
            scrolls['adm_no'].text='No such student in database !'
            scrolls['clas'].text=''
            scrolls['id_no'].text=''
            scrolls['name'].text=''
            self.current_std_issue.ids.lbltitle.text=' Current borrowed books '
            self.history_std_issue.ids.lbltitle.text=' History of books'

    #loads current borrowed books
    def show_current_books(self,scrolls,gridl,current,soo,*args):
        #refresh the database first
        self.timer_start_work_notification()
        if soo=='s':
            self.cursor.execute(''' SELECT book_accession_no, date_issued, date_suppossed_return, date_passed_by, adm_no, id_no, by_user  FROM borrow WHERE adm_no=? ''',(scrolls['adm_no'].text,))
        else:
            self.cursor.execute(''' SELECT book_accession_no, date_issued, date_suppossed_return, date_passed_by, adm_no, id_no, by_user  FROM borrow WHERE id_no=? ''',(scrolls['id_no'].text,))
        book_acc_no=self.cursor.fetchall()
        
        if soo=='s':
            self.cursor.execute(''' SELECT name FROM members WHERE adm_no=? ''',(scrolls['adm_no'].text,))
        else:
            self.cursor.execute(''' SELECT name FROM members WHERE id_no=? ''',(scrolls['id_no'].text,))
        name=self.cursor.fetchall()
        
        current.ids.lbltitle.text='%s current borrowed books(%s)'%(name[0][0], len(book_acc_no))
        gridl.clear_widgets()

        for books in book_acc_no:
            self.cursor.execute(''' SELECT title, publisher,lost,damaged FROM books WHERE book_accession_no=?''',(books[0],))
            det=self.cursor.fetchall()
                
            #check if book is lost
            print(det, books[0])
            if det[0][2]=='yes':
                if soo=='s':
                    self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'student', size_hint=(1,None), size=(1,220))
                    self.BorrowB.member_type='student'
                    self.BorrowB.ids.pers.text='Admission no. :'
                    self.BorrowB.ids.adm_id.text=books[4]
                elif soo=='t':
                    self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'teacher', size_hint=(1,None), size=(1,220))
                    self.BorrowB.member_type='teacher'
                    self.BorrowB.ids.pers.text='Id no. :'
                    self.BorrowB.ids.adm_id.text=books[5]
                else:
                    self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'Non teaching stuff', size_hint=(1,None), size=(1,220))
                    self.BorrowB.member_type='Non teaching stuff'
                    self.BorrowB.ids.pers.text='Id no. :'
                    self.BorrowB.ids.adm_id.text=books[5]
                self.BorrowB.ids.imgb.source='pics\\book_lost.png'
                self.BorrowB.ids.marklost.text='Unmark book as lost'
                threading.Thread(target=self.show_current_borrowed_books,args=(self.BorrowB,gridl,)).start()
            else:
                if det[0][3]=='yes':
                    if soo=='s':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'student', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='student'
                        self.BorrowB.ids.pers.text='Admission no. :'
                        self.BorrowB.ids.adm_id.text=books[4]
                    elif soo=='t':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'teacher', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='teacher'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    else:
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'Non teaching stuff', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='Non teaching stuff'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    self.BorrowB.ids.imgb.source='pics\\book_damaged.png'
                    self.BorrowB.ids.markdamaged.text='Unmark book as damaged'
                    threading.Thread(target=self.show_current_borrowed_books,args=(self.BorrowB,gridl,)).start()

                else:
                    if soo=='s':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'student', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='student'
                        self.BorrowB.ids.pers.text='Admission no. :'
                        self.BorrowB.ids.adm_id.text=books[4]
                    elif soo=='t':
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'teacher', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='teacher'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    else:
                        self.BorrowB=BorrowButton(books[0], det[0][0], det[0][1], books[1], books[2], books[3], books[6], 'Non teaching stuff', size_hint=(1,None), size=(1,220))
                        self.BorrowB.member_type='Non teaching stuff'
                        self.BorrowB.ids.pers.text='Id no. :'
                        self.BorrowB.ids.adm_id.text=books[5]
                    self.BorrowB.ids.imgb.source='pics\\book.png'

                    #change color when book is due
                    if int(books[3]) >0:
                        self.BorrowB.ids.imgb.color = 139/255, 126/255, 102/255,1  
                    
                    threading.Thread(target=self.show_current_borrowed_books,args=(self.BorrowB,gridl,)).start()
                    

    def show_current_borrowed_books(self,BorrowB,gridl,*args):
        gridl.add_widget(self.BorrowB)

    #return book function
    def return_book(self,acc_n,titl,publ,date_iss,date_supp,date_pass,mtype,adm_id,marklost):
        self.cursor.execute(''' SELECT lost FROM books WHERE book_accession_no=? ''',(acc_n,))
        lost=self.cursor.fetchall()
        if lost[0][0]=='yes':
            #check if book is lost
            content = MDLabel(font_style='Caption',text="Please unmark the book as not lost first to return the book", size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Unmark book as lost !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=False)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
            self.dialog.open()
        else:
            self.cursor.execute(''' SELECT damaged FROM books WHERE book_accession_no=? ''',(acc_n,))
            damaged = self.cursor.fetchall()

            if damaged[0][0]=='yes':
                #check if book is dmaged
                content = MDLabel(font_style='Caption',text="Please Unmark the book as damaged first to return the book", size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Unmark book as damaged !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=False)
                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                self.dialog.open()
            else:
                content = MDLabel(font_style='Caption',text="Are you sure you want to return %s book accession number %s"%(titl,acc_n), size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Confirm ",content=content,size_hint=(.4, None),height=(200),auto_dismiss=False)
                self.dialog.add_action_button("no",action=lambda *x: self.dialog.dismiss())
                self.dialog.add_action_button("yes",action=lambda *x: self.return_book2(acc_n,titl,publ,date_iss,date_supp,date_pass,mtype,adm_id))        
                self.dialog.open()

    def return_book2(self,acc_n,titl,publ,date_iss,date_supp,date_pass,mtype,adm_id,*args):
        self.dialog.dismiss()
        #update book as not borrowed
        self.cursor.execute(''' UPDATE books SET borrowed='no', borrowed_by='none' WHERE book_accession_no=? ''',(acc_n,))
        self.connection.commit()
        #delete member borrowing record
        self.cursor.execute(''' DELETE FROM borrow WHERE book_accession_no=? ''',(acc_n,))
        self.connection.commit()
        #add record to history
        today_date=str(datetime.datetime.now())[:10]
        if mtype=='student':
            self.cursor.execute(''' INSERT INTO history(book_accession_no, adm_no, id_no,  date_issued, date_suppossed_return, date_returned, date_passed_by, by_user)\
                                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',\
                                (acc_n, adm_id, 'none', date_iss, date_supp, today_date, date_pass, self.user_name,))
        else:
            self.cursor.execute(''' INSERT INTO history(book_accession_no, adm_no, id_no,  date_issued, date_suppossed_return, date_returned, date_passed_by, by_user)\
                                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',\
                                (acc_n, 'none', adm_id, date_iss, date_supp, today_date, date_pass, self.user_name,))   
        self.connection.commit()
        #remove widget from layout
        self.Gridlayout_std_issue.clear_widgets()
        #load borrowed books
        if mtype=='student':
            self.show_current_books(self.wid_std_circ_scrolls,self.Gridlayout_std_issue,self.current_std_issue,'s')
        elif mtype=='teacher':
            self.show_current_books(self.wid_teach_circ_scrolls,self.Gridlayout_teach_issue,self.current_Teachers_issue,'t')
        else:
            self.show_current_books(self.wid_non_circ_scrolls,self.Gridlayout_non_issue,self.current_non_issue,'n')
            

    #load all history
    def show_history_books(self,soo,*args):
        if soo=='s':
            #load history
            self.load_history_book(self.wid_mem_std_scrolls, self.Gridlayout_std_history, self.history_std_issue,'s')
        elif soo=='t':
            #load history controls
            self.load_history_book(self.wid_mem_teachers_scrolls, self.Gridlayout_teach_history, self.history_teach_issue,'t')
        else:
            #load history controls
            self.load_history_book(self.wid_mem_non_scrolls, self.Gridlayout_non_history, self.history_non_issue,'n')
        
    #Load history of books
    def load_history_book(self,scrolls,gridl,hist_books,soo,*args):
        #fetch everything from table history
        if soo=='s':
            self.cursor.execute(''' SELECT * FROM history WHERE adm_no=?''',(scrolls['adm_no'].text,))
        else:
            self.cursor.execute(''' SELECT * FROM history WHERE id_no=?''',(scrolls['id_no'].text,))
        hist_rec=self.cursor.fetchall()
        if soo=='s':
            self.cursor.execute(''' SELECT name FROM members WHERE adm_no=?''',(scrolls['adm_no'].text,))
        else:
            self.cursor.execute(''' SELECT name FROM members WHERE id_no=?''',(scrolls['id_no'].text,))
        name=self.cursor.fetchall()
        if len(name) != 0:
            hist_books.ids.lbltitle.text='%s book history '%name[0][0]
        gridl.clear_widgets()
    
        for rec in hist_rec:
        #fetch books details from table books
            self.cursor.execute(''' SELECT title, publisher FROM books WHERE book_accession_no=? ''',(rec[1],))
            rec_bd=self.cursor.fetchall()
            Histotyb=HistoryButton(rec[1], rec_bd[0][0], rec_bd[0][1], rec[4], rec[5], rec[6], rec[7], size_hint=(1,None),size=(1,100))
            Histotyb.ids.imgb.source='pics\\book_history.png'
            threading.Thread(target=self.load_histry_buttons,args=(gridl,Histotyb,)).start()

    def load_histry_buttons(self,gridl,Historyb,*args):
        gridl.add_widget(Historyb)

    #mark book as lost
    def mark_book_as_lost(self,acc_n,adm_id,marklost,imgb,member_type):
        content = MDLabel(font_style='Caption',text="Are you sure you want to change book accession no. %s lost status"%acc_n, size_hint=(1,None),valign='middle',halign='left',markup=True)
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Confirm !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
        self.dialog.add_action_button("Yes",action=lambda *x: self.authenticated_mark_as_lost(acc_n,adm_id,marklost,imgb,member_type))
        self.dialog.add_action_button("No",action=lambda *x: self.dialog.dismiss())
        self.dialog.open()


    def authenticated_mark_as_lost(self,acc_n,adm_id,marklost,imgb,member_type):
        self.dialog.dismiss()
        #update table books as lost or unlost
        self.cursor.execute(''' SELECT damaged FROM books WHERE book_accession_no =? ''',(acc_n,))
        lost_det=self.cursor.fetchall()

        if lost_det[0][0] =='yes':
            content = MDLabel(font_style='Caption',text="Mark the book as not damaged to proceed.", size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Logical error !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            if marklost.text=='Mark book as lost':
                imgb.source='pics\\book_lost.png'
                self.cursor.execute(''' UPDATE books SET lost='yes',lost_by=? WHERE book_accession_no=? ''',(adm_id,acc_n,))
                self.connection.commit()
                marklost.text='Unmark book as lost'
            else:
                imgb.source='pics\\book.png'
                self.cursor.execute(''' UPDATE books SET lost='no', lost_by="none" WHERE book_accession_no=? ''',(acc_n,))
                self.connection.commit()
                marklost.text='Mark book as lost'

    #mark book as damaged
    def mark_book_as_damaged(self,acc_n,adm_id,markdamaged,imgb,member_type):
        content = MDLabel(font_style='Caption',text="Are you sure you want to change book accession no. %s damaged status"%acc_n, size_hint=(1,None),valign='middle',halign='left',markup=True)
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Confirm !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
        self.dialog.add_action_button("Yes",action=lambda *x: self.authenticated_damaged_book(acc_n,adm_id,markdamaged,imgb,member_type))
        self.dialog.add_action_button("No",action=lambda *x: self.dialog.dismiss())
        self.dialog.open()



    def authenticated_damaged_book(self,acc_n,adm_id,markdamaged,imgb,member_type):
        self.dialog.dismiss()
        #update table books as damaged or not damaged
        self.cursor.execute(''' SELECT lost FROM books WHERE book_accession_no =? ''',(acc_n,))
        lost_det=self.cursor.fetchall()

        if lost_det[0][0] =='yes':
            content = MDLabel(font_style='Caption',text="The book is not in existence. A book cannot be both lost and damaged.", size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Logical error !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()            
        else:
            if markdamaged.text=='Mark book as damaged':
                imgb.source='pics\\book_damaged.png'
                self.cursor.execute(''' UPDATE books SET damaged='yes', damaged_by=? WHERE book_accession_no=? ''',(adm_id,acc_n,))
                self.connection.commit()
                markdamaged.text='Unmark book as damaged'
            else:
                imgb.source='pics\\book.png'
                self.cursor.execute(''' UPDATE books SET damaged='no', damaged_by="none" WHERE book_accession_no=? ''',(acc_n,))
                self.connection.commit()
                markdamaged.text='Mark book as damaged'    

    #clear the form
    def clear_form_circ(self,controls,soo,*args):
        if soo=='s':
            controls['adm_no'].text=''
            controls['name'].text=''
            controls['id_no'].text=''
            controls['clas'].text=''
            controls['book_acc_no'].text=''
            controls['titl'].text=''
            controls['pub'].text=''
        else:
            controls['name'].text=''
            controls['id_no'].text=''
            controls['book_acc_no'].text=''
            controls['titl'].text=''
            controls['pub'].text=''
            
    #update the circulation records
    def update_record_circ(self,controls,*args):
        if controls['dat_issue'].text =='None' or controls['date_ret'].text =='None':
            content = MDLabel(font_style='Caption',text="Make sure that the date issued and suppossed to return are not 'None'",
                                                                          size_hint=(1,None),valign='middle',halign='left',markup=True)
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Error ! ",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            if controls['book_acc_no'].text !='':
                content = MDLabel(font_style='Caption',text='Only the date issued and date supposed to returned will be updated, do you want to proceed',
                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Update ",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                self.dialog.add_action_button("No",action=lambda *x: self.dialog.dismiss())
                self.dialog.add_action_button("Yes",action=lambda *x: self.update_rec_circ(controls))
                self.dialog.open()

    def update_rec_circ(self,controls,*args):
        self.cursor.execute(''' UPDATE borrow SET date_issued =?, date_suppossed_return=? WHERE book_accession_no=? ''',\
                               (controls['dat_issue'].text, controls['date_ret'].text, controls['book_acc_no'].text,))
        self.connection.commit()
        self.dialog.dismiss()
        
            
        
    #mark the account either activate or deactivated
    def mark_the_padlocks(self, scrolls, soo):
        if soo=='s':
            self.cursor.execute(''' SELECT deactivate FROM members WHERE adm_no=? ''',(scrolls['adm_no'].text,))
            switch=self.cursor.fetchall()
            if switch[0][0]=='yes':   
                self.actd_std0.color=(0,0,0,.83)
                self.actd_std.color=(1,0,0,.83)
            else:
                self.actd_std0.color=(0,1,0,.83)
                self.actd_std.color=(0,0,0,.83)
                
        elif soo=='t':
            self.cursor.execute(''' SELECT deactivate FROM members WHERE id_no=? ''',(scrolls['id_no'].text,))
            switch=self.cursor.fetchall()
            if switch[0][0]=='yes':   
                self.actd_teach0.color=(0,0,0,.83)
                self.actd_teach.color=(1,0,0,.83)
            else:
                self.actd_teach0.color=(0,1,0,.83)
                self.actd_teach.color=(0,0,0,.83)
        else:
            self.cursor.execute(''' SELECT deactivate FROM members WHERE id_no=? ''',(scrolls['id_no'].text,))
            switch=self.cursor.fetchall()
            if switch[0][0]=='yes':   
                self.actd_non0.color=(0,0,0,.83)
                self.actd_non.color=(1,0,0,.83)
            else:
                self.actd_non0.color=(0,1,0,.83)
                self.actd_non.color=(0,0,0,.83)
                
            
    def move_to_first_record_circ(self,controls,nav,soo,*args):
        #fetch the students details
        if soo=='s':
            self.cursor.execute('''SELECT * FROM borrow WHERE member_type="student" ORDER BY id ASC LIMIT 1''')
        elif soo=='t':
            self.cursor.execute('''SELECT * FROM borrow WHERE member_type="teacher" ORDER BY id ASC LIMIT 1''')
        else:
            self.cursor.execute('''SELECT * FROM borrow WHERE member_type="non" ORDER BY id ASC LIMIT 1''')    
        rec=self.cursor.fetchall()
        lis=rec
        
        #chek if there is no record
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            #fetch books details
            self.cursor.execute('''SELECT title, publisher FROM books WHERE book_accession_no =? ''',(rec[0][7],))
            book_det=self.cursor.fetchall()
            book_det=book_det[0]

            #fetch member name,class
            if soo=='s':
                self.cursor.execute(''' SELECT name,class FROM members WHERE adm_no =? ''',(rec[0][1],))
            else:
                self.cursor.execute(''' SELECT name,class FROM members WHERE id_no =? ''',(rec[0][2],))
            member_details=self.cursor.fetchall()
            member_details=member_details[0]

            
            recs=lis[0]
            # fill the forms
            if soo=='s':
                controls['adm_no'].text=str(recs[1])
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['clas'].text=str(member_details[1])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
            else:
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
                
            #accumulate the counter by one and load the image
            if soo=='s':
                self.index_std_circ=recs[0]
                file=open('index_std_circ.txt','w')
                file.write(str(self.index_std_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['adm_no'].text
            
                if req_pic not in self.std_pics:
                    self.img_std_issue.img.source='pics\\account.png'
                else:
                    self.img_std_issue.img.source='std_pic\\%s.jpg'%controls['adm_no'].text
                    self.img_std_issue.img.reload()
                self.mark_the_padlocks(controls,'s')
            elif soo=='t':
                self.index_teach_circ=recs[0]
                file=open('index_teach_circ.txt','w')
                file.write(str(self.index_teach_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers_issue.img.source='pics\\account.png'
                else:
                    self.img_teachers_issue.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers_issue.img.reload()
                self.mark_the_padlocks(controls,'t')
            else:
                self.index_non_circ=recs[0]
                file=open('index_non_circ.txt','w')
                file.write(str(self.index_non_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching_issue.img.source='pics\\account.png'
                else:
                    self.img_non_teaching_issue.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching_issue.img.reload()
                self.mark_the_padlocks(controls,'n')
        
        
    def move_to_last_record_circ(self,controls,nav,soo,*args):
        #fetch the students details
        if soo=='s':
            self.cursor.execute('''SELECT * FROM borrow WHERE member_type="student" ORDER BY id DESC LIMIT 1''')
        elif soo=='t':
            self.cursor.execute('''SELECT * FROM borrow WHERE member_type="teacher" ORDER BY id DESC LIMIT 1''')
        else:
            self.cursor.execute('''SELECT * FROM borrow WHERE member_type="non" ORDER BY id DESC LIMIT 1''')    
        rec=self.cursor.fetchall()
        lis=rec
        
        #chek if there is no record
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            #fetch books details
            self.cursor.execute('''SELECT title, publisher FROM books WHERE book_accession_no =? ''',(rec[0][7],))
            book_det=self.cursor.fetchall()
            book_det=book_det[0]

            #fetch member name,class
            if soo=='s':
                self.cursor.execute(''' SELECT name,class FROM members WHERE adm_no =? ''',(rec[0][1],))
            else:
                self.cursor.execute(''' SELECT name,class FROM members WHERE id_no =? ''',(rec[0][2],))
            member_details=self.cursor.fetchall()
            member_details=member_details[0]
            
            recs=lis[0]
            # fill the forms
            if soo=='s':
                controls['adm_no'].text=str(recs[1])
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['clas'].text=str(member_details[1])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
            else:
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
                
            #accumulate the counter by one and load the image
            if soo=='s':
                self.index_std_circ=recs[0]
                file=open('index_std_circ.txt','w')
                file.write(str(self.index_std_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['adm_no'].text
            
                if req_pic not in self.std_pics:
                    self.img_std_issue.img.source='pics\\account.png'
                else:
                    self.img_std_issue.img.source='std_pic\\%s.jpg'%controls['adm_no'].text
                    self.img_std_issue.img.reload()
                self.mark_the_padlocks(controls,'s')
                
            elif soo=='t':
                self.index_teach_circ=recs[0]
                file=open('index_teach_circ.txt','w')
                file.write(str(self.index_teach_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers_issue.img.source='pics\\account.png'
                else:
                    self.img_teachers_issue.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers_issue.img.reload()
                self.mark_the_padlocks(controls,'t')
            else:
                self.index_non_circ=recs[0]
                file=open('index_non_circ.txt','w')
                file.write(str(self.index_non_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching_issue.img.source='pics\\account.png'
                else:
                    self.img_non_teaching_issue.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching_issue.img.reload()
                self.mark_the_padlocks(controls,'n')
                    

    def move_to_prev_record_circ(self,controls,nav,soo,*args):
        #fetch the students details
        if soo=='s':
            self.cursor.execute('''SELECT * FROM borrow WHERE id < ? AND member_type="student" ORDER BY id DESC LIMIT 1''',(self.index_std_circ,))
        elif soo=='t':
            self.cursor.execute('''SELECT * FROM borrow WHERE id < ? AND member_type="teacher" ORDER BY id DESC LIMIT 1''',(self.index_teach_circ,))
        else:
            self.cursor.execute('''SELECT * FROM borrow WHERE id < ? AND member_type="non" ORDER BY id DESC LIMIT 1''',(self.index_non_circ,))    
        rec=self.cursor.fetchall()
        lis=rec
        
        #chek if there is no record
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the first record ! [/b]',1)
        else:
            #fetch books details
            self.cursor.execute('''SELECT title, publisher FROM books WHERE book_accession_no =? ''',(rec[0][7],))
            book_det=self.cursor.fetchall()
            book_det=book_det[0]

            #fetch member name,class
            if soo=='s':
                self.cursor.execute(''' SELECT name,class FROM members WHERE adm_no =? ''',(rec[0][1],))
            else:
                self.cursor.execute(''' SELECT name,class FROM members WHERE id_no =? ''',(rec[0][2],))
            member_details=self.cursor.fetchall()
            member_details=member_details[0]
            
            recs=lis[0]
            # fill the forms
            if soo=='s':
                controls['adm_no'].text=str(recs[1])
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['clas'].text=str(member_details[1])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
            else:
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
                
            #accumulate the counter by one and load the image
            if soo=='s':
                self.index_std_circ=recs[0]
                file=open('index_std_circ.txt','w')
                file.write(str(self.index_std_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['adm_no'].text
            
                if req_pic not in self.std_pics:
                    self.img_std_issue.img.source='pics\\account.png'
                else:
                    self.img_std_issue.img.source='std_pic\\%s.jpg'%controls['adm_no'].text
                    self.img_std_issue.img.reload()
                self.mark_the_padlocks(controls,'s')
                
            elif soo=='t':
                self.index_teach_circ=recs[0]
                file=open('index_teach_circ.txt','w')
                file.write(str(self.index_teach_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers_issue.img.source='pics\\account.png'
                else:
                    self.img_teachers_issue.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers_issue.img.reload()
                self.mark_the_padlocks(controls,'t')
                
            else:
                self.index_non_circ=recs[0]
                file=open('index_non_circ.txt','w')
                file.write(str(self.index_non_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching_issue.img.source='pics\\account.png'
                else:
                    self.img_non_teaching_issue.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching_issue.img.reload()
                self.mark_the_padlocks(controls,'n')
        
    def move_to_next_record_circ(self,controls,nav,soo,*args):
        #fetch the students details
        if soo=='s':
            self.cursor.execute('''SELECT * FROM borrow WHERE id > ? AND member_type="student" ORDER BY id ASC LIMIT 1''',(self.index_std_circ,))
        elif soo=='t':
            self.cursor.execute('''SELECT * FROM borrow WHERE id > ? AND member_type="teacher" ORDER BY id ASC LIMIT 1''',(self.index_teach_circ,))
        else:
            self.cursor.execute('''SELECT * FROM borrow WHERE id > ? AND member_type="non" ORDER BY id ASC LIMIT 1''',(self.index_non_circ,))    
        rec=self.cursor.fetchall()
        lis=rec
        
        #chek if there is no record
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            #fetch books details
            self.cursor.execute('''SELECT title, publisher FROM books WHERE book_accession_no =? ''',(rec[0][7],))
            book_det=self.cursor.fetchall()
            book_det=book_det[0]

            #fetch member name,class
            if soo=='s':
                self.cursor.execute(''' SELECT name,class FROM members WHERE adm_no =? ''',(rec[0][1],))
            else:
                self.cursor.execute(''' SELECT name,class FROM members WHERE id_no =? ''',(rec[0][2],))
            member_details=self.cursor.fetchall()
            member_details=member_details[0]
            
            recs=lis[0]
            # fill the forms
            if soo=='s':
                controls['adm_no'].text=str(recs[1])
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['clas'].text=str(member_details[1])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
            else:
                controls['name'].text=str(member_details[0])
                controls['id_no'].text=str(recs[2])
                controls['book_acc_no'].text=str(recs[7])
                controls['titl'].text=str(book_det[0])
                controls['pub'].text=str(book_det[1])
                controls['dat_issue'].text=str(recs[3])
                controls['date_ret'].text=str(recs[5])
                
            #accumulate the counter by one and load the image
            if soo=='s':
                self.index_std_circ=recs[0]
                file=open('index_std_circ.txt','w')
                file.write(str(self.index_std_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['adm_no'].text
            
                if req_pic not in self.std_pics:
                    self.img_std_issue.img.source='pics\\account.png'
                else:
                    self.img_std_issue.img.source='std_pic\\%s.jpg'%controls['adm_no'].text
                    self.img_std_issue.img.reload()
                self.mark_the_padlocks(controls,'s')
                
            elif soo=='t':
                self.index_teach_circ=recs[0]
                file=open('index_teach_circ.txt','w')
                file.write(str(self.index_teach_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers_issue.img.source='pics\\account.png'
                else:
                    self.img_teachers_issue.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers_issue.img.reload()
                self.mark_the_padlocks(controls,'t')
                
            else:
                self.index_non_circ=recs[0]
                file=open('index_non_circ.txt','w')
                file.write(str(self.index_non_circ))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching_issue.img.source='pics\\account.png'
                else:
                    self.img_non_teaching_issue.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching_issue.img.reload()
                self.mark_the_padlocks(controls,'n')
  
    #record for combined circulation
    def combined_circ_add_rec(self,scrolls,nav,inputs,soo,*args):
        #check if person is registered
        if soo=='s':
            self.cursor.execute(''' SELECT * FROM members WHERE adm_no=? ''',(scrolls['adm_no'].text,))
        else:
            self.cursor.execute(''' SELECT * FROM members WHERE id_no=? ''',(scrolls['id_no'].text,))
        reg_chk=self.cursor.fetchall()
        reg_chk_no=len(reg_chk)

        if reg_chk_no ==0:
            self.show_nav_anim(nav,'pics\\noti_error.png',\
                                                  '[b]Member not registered ![/b] [i]Please register the member first[/i]',5,inputs)
        else:
            #check if book is registered
            self.cursor.execute(''' SELECT * FROM books WHERE book_accession_no=? ''',(scrolls['book_acc_no'].text,))
            reg_chk=self.cursor.fetchall()
            reg_chk_no=len(reg_chk)
            
            if reg_chk_no ==0:
                self.show_nav_anim(nav,'pics\\noti_error.png',\
                                                  '[b]Book not registered ![/b] [i]Please register the book first[/i]',5,inputs)
            else:
                #check if the person has reached the max borrowing time
                if soo=='s':
                    self.cursor.execute(''' SELECT COUNT(*) FROM borrow WHERE adm_no = ? ''',(scrolls['adm_no'].text,))
                else:
                    self.cursor.execute(''' SELECT COUNT(*) FROM borrow WHERE id_no=? ''',(scrolls['id_no'].text,))

                times_borrowed = self.cursor.fetchall()[0][0]

                if soo=='s':
                    if times_borrowed >= self.times_borrowed[0]:
                        exceed_limit = 'yes'
                    else:
                        exceed_limit = 'no'
                        
                elif soo=='t':
                    if times_borrowed >= self.times_borrowed[1]:
                        exceed_limit = 'yes'
                    else:
                        exceed_limit = 'no'
                    
                elif soo=='n':
                    if times_borrowed >= self.times_borrowed[2]:
                        exceed_limit = 'yes'
                    else:
                        exceed_limit = 'no'
                print('times borrowed', times_borrowed, 'no times', self.times_borrowed )
                if exceed_limit =='yes':
                    if soo =='s':
                        content = MDLabel(font_style='Caption',text='Borrowing more than %s times is not allowed to students'%self.times_borrowed[0],
                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                    elif soo =='t':
                        content = MDLabel(font_style='Caption',text='Borrowing more than %s times is not allowed to teachers'%self.times_borrowed[1],
                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                    elif soo =='n':
                        content = MDLabel(font_style='Caption',text='Borrowing more than %s times is not allowed to non teaching stuff'%self.times_borrowed[2],
                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                    
                    content.bind(texture_size=content.setter('size'))
                    self.dialog = MDDialog(title="Failed !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                    self.dialog.open()

                else:
        
                    #check if the book is lost
                    self.cursor.execute(''' SELECT lost,title,lost_by FROM books WHERE book_accession_no=? ''',(scrolls['book_acc_no'].text,))
                    rec_lost=self.cursor.fetchall()
                    
                    if rec_lost[0][0]=='yes':
                        content = MDLabel(font_style='Caption',text='[b]%s[/b] is lost by [b]%s[/b] '%(rec_lost[0][1], rec_lost[0][2]),
                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                        content.bind(texture_size=content.setter('size'))
                        self.dialog = MDDialog(title="Book is lost !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                        self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                        self.dialog.open()
                    else:
                        #check if the book is borrowed
                        self.cursor.execute(''' SELECT borrowed, borrowed_by,title FROM books WHERE book_accession_no=? ''',(scrolls['book_acc_no'].text,))
                        rec_borrow=self.cursor.fetchall()
                        if rec_borrow[0][0]=='yes':
                            
                            content = MDLabel(font_style='Caption',text='[b]%s[/b] is already borrowed by [b]%s[/b] '%(rec_borrow[0][2], rec_borrow[0][1]),
                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                            content.bind(texture_size=content.setter('size'))
                            self.dialog = MDDialog(title="Book is already borrowed !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                            self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                            self.dialog.open()
                        else:
                            #check if the date supposed to return has the valid format
                            formt= re.compile('.*/.*/.*')
                            if formt.match(scrolls['date_ret'].text) is None:
                                content = MDLabel(font_style='Caption',text='Click the date suppossed to return to pick a date',\
                                                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                                content.bind(texture_size=content.setter('size'))
                                self.dialog = MDDialog(title="Invalid date !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                                self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                                self.dialog.open()
                            else:
                                #check if the member is deactivated
                                if soo=='s':
                                    self.cursor.execute(''' SELECT deactivate, date_deactivate FROM members WHERE adm_no =? ''',(scrolls['adm_no'].text,))
                                    rec_deact=self.cursor.fetchall()
                                else:
                                    self.cursor.execute(''' SELECT deactivate, date_deactivate FROM members WHERE id_no =? ''',(scrolls['id_no'].text,))
                                    rec_deact=self.cursor.fetchall()

                                if rec_deact[0][0] =='yes':
                                    content = MDLabel(font_style='Caption',text='This member account was deactivated on %s . Activate his account to enable borrowing'%rec_deact[0][1],\
                                                                                                              size_hint=(1,None),valign='middle',halign='left',markup=True)
                                    content.bind(texture_size=content.setter('size'))
                                    self.dialog = MDDialog(title="Account is Deactivated !",content=content,size_hint=(.4, None),height=(200),auto_dismiss=True)
                                    self.dialog.add_action_button("Ok",action=lambda *x: self.dialog.dismiss())                            
                                    self.dialog.open()
                                else:
                                    #now add the record to table borrowed plus update the books table as book is borrowed and borrowed by who
                                    #add record
                                    if soo=='s':
                                        adm=scrolls['adm_no'].text
                                    id_no=scrolls['id_no'].text
                                    date_issue=scrolls['dat_issue'].text
                                    date_sup_ret=scrolls['date_ret'].text
                                    acc_no=scrolls['book_acc_no'].text
                                    user=self.user_name
                                    
                                    if soo=='s':
                                        self.cursor.execute(''' INSERT INTO borrow(adm_no, id_no, date_issued, date_suppossed_return, book_accession_no, by_user, member_type)\
                                                            VALUES(?, ?, ?, ?, ?, ?, ?) ''',(adm, id_no, date_issue, date_sup_ret, acc_no,user, 'student',))
                                        #load borrowed books
                                        self.show_current_books(scrolls,self.Gridlayout_std_issue,self.current_std_issue,'s')
                                    elif soo=='t':
                                        self.cursor.execute(''' INSERT INTO borrow( id_no, date_issued, date_suppossed_return, book_accession_no, by_user, member_type)\
                                                            VALUES(?, ?, ?, ?, ?, ?) ''',( id_no, date_issue, date_sup_ret, acc_no,user, 'teacher',))
                                        #load borrowed books
                                        self.show_current_books(scrolls,self.Gridlayout_teach_issue,self.current_Teachers_issue,'t')
                                    else:
                                        self.cursor.execute(''' INSERT INTO borrow( id_no, date_issued, date_suppossed_return, book_accession_no, by_user, member_type)\
                                                            VALUES(?, ?, ?, ?, ?, ?) ''',( id_no, date_issue, date_sup_ret, acc_no,user, 'non',))
                                        #load borrowed books
                                        self.show_current_books(scrolls,self.Gridlayout_non_issue,self.current_non_issue,'n')
                                        
                                    self.connection.commit()
                                    
                                    #update book as borrowed
                                    if soo=='s':
                                        self.cursor.execute(''' UPDATE books SET borrowed=?, borrowed_by=? WHERE book_accession_no=?''',('yes',adm,acc_no,))
                                    else:
                                        self.cursor.execute(''' UPDATE books SET borrowed=?, borrowed_by=? WHERE book_accession_no=?''',('yes',id_no,acc_no,))

                                    self.connection.commit()

                                    
                                    self.show_nav_anim(nav,'pic_control\\tick.png',\
                                                              'Book borrowed successfully',2,inputs)
                                    self.backup_counter+=1
                                    #save the backup_counter
                                    a=open('backup_counter.txt','w')
                                    a.write(str(self.backup_counter))
                                    a.close()

                                    if self.ids.apply_b_i.active==True:
                                        scrolls['book_acc_no'].text=''
                                        if soo=='s':
                                            scrolls['adm_no'].text=''
                                            scrolls['adm_no'].focus=True
                                            scrolls['name'].text=''
                                            scrolls['clas'].text=''
                                            scrolls['titl'].text=''
                                            scrolls['pub'].text=''
                                        else:
                                            scrolls['id_no'].text=''
                                            scrolls['id_no'].focus=True
                                            scrolls['name'].text=''
                                            scrolls['titl'].text=''
                                            scrolls['pub'].text=''
                                    
                                    
    ################################################ SEARCH FOR CONTENTS IN DATABASE
    #one book registration
    def display_results_one_book(self,*args):
        value=self.one_book_scroll_inputs['acc_n'].text
        self.cursor.execute('''SELECT * FROM books WHERE book_accession_no = ? ''',(value,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)
        
        controls=self.one_book_scroll_inputs
        if rec_no!=0:
            recs=rec[rec_no-1]
            controls['isbn'].text=str(recs[2])
            controls['tit'].text=str(recs[3])
            controls['pubr'].text=str(recs[4])
            controls['edition'].text=str(recs[5])
            controls['auth'].text=str(recs[6])
            controls['pob'].text=str(recs[7])
            controls['yop'].text=str(recs[8])
            controls['categ'].text=str(recs[9])
            controls['shelve'].text=str(recs[10])
        else:
            controls['acc_n'].text='No record found !'
            controls['isbn'].text=''
            controls['tit'].text=''
            controls['pubr'].text=''
            controls['edition'].text=''
            controls['auth'].text=''
            controls['pob'].text=''
            controls['yop'].text=''
            controls['categ'].text=''
            controls['shelve'].text=''

    #many book registration
    def display_results_many_book(self,*args):
        value=self.many_book_scroll_inputs['acc_n'].text
        self.cursor.execute('''SELECT * FROM books WHERE book_accession_no = ? ''',(value,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)
        
        controls=self.many_book_scroll_inputs
        if rec_no!=0:
            recs=rec[rec_no-1]
            controls['isbn'].text=str(recs[2])
            controls['tit'].text=str(recs[3])
            controls['pubr'].text=str(recs[4])
            controls['edition'].text=str(recs[5])
            controls['auth'].text=str(recs[6])
            controls['pob'].text=str(recs[7])
            controls['yop'].text=str(recs[8])
            controls['categ'].text=str(recs[9])
            controls['shelve'].text=str(recs[10])
        else:
            controls['acc_n'].text='No record found !'
            controls['isbn'].text=''
            controls['tit'].text=''
            controls['pubr'].text=''
            controls['edition'].text=''
            controls['auth'].text=''
            controls['pob'].text=''
            controls['yop'].text=''
            controls['categ'].text=''
            controls['shelve'].text=''

    #students search
    def display_results_std_book(self,*args):
        value=self.wid_mem_std_scrolls['adm_no'].text
        self.cursor.execute('''SELECT * FROM members WHERE adm_no LIKE ? AND member_type="student"  ''',('%'+value+'%',))
        rec=self.cursor.fetchall()
        rec_no=len(rec)
        
        scrolls=self.wid_mem_std_scrolls
        
        if rec_no!=0:
            recs=rec[rec_no-1]
            scrolls['adm_no'].text=str(recs[1])
            scrolls['clas'].text=str(recs[2])
            scrolls['id_no'].text=str(recs[3])
            scrolls['name'].text=str(recs[4])
            
            #sets the gender
            if recs[5]=='M':
                scrolls['gender_female'].active=False
                scrolls['gender_male'].active=True
            else:
                scrolls['gender_female'].active=True
                scrolls['gender_male'].active=False
                
            #load image
            req_pic='%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
            if req_pic not in self.std_pics:
                self.img_std.img.source='pics\\account.png'
            else:
                self.img_std.img.reload()
                self.img_std.img.source='std_pic\\%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
        else:
            scrolls['adm_no'].text='No record found !'
            scrolls['clas'].text=''
            scrolls['id_no'].text=''
            scrolls['name'].text=''
            self.img_std.img.source='pics\\account.png'
        
    #teachers
    def display_results_teach_book(self,*args):
        value=self.wid_mem_teachers_scrolls['id_no'].text
        self.cursor.execute('''SELECT * FROM members WHERE id_no LIKE ? AND member_type="teacher"  ''',(value+'%',))
        rec=self.cursor.fetchall()
        rec_no=len(rec)
        
        scrolls=self.wid_mem_teachers_scrolls
        
        if rec_no!=0:
            recs=rec[rec_no-1]
            scrolls['id_no'].text=str(recs[3])
            scrolls['name'].text=str(recs[4])
            
            #sets the gender
            if recs[5]=='M':
                scrolls['gender_female'].active=False
                scrolls['gender_male'].active=True
            else:
                scrolls['gender_female'].active=True
                scrolls['gender_male'].active=False
                
            #load image
            req_pic='%s.jpg'%self.wid_mem_teachers_scrolls['id_no'].text
            
            if req_pic not in self.teach_pics:
                self.img_teachers.img.source='pics\\account.png'
            else:
                self.img_teachers.img.reload()
                self.img_teachers.img.source='teach_pic\\%s.jpg'%self.wid_mem_teachers_scrolls['id_no'].text
        else:
            scrolls['id_no'].text='No record found !'
            scrolls['name'].text=''
            self.img_teachers.img.source='pics\\account.png'

    #non teaching
    def display_results_non_book(self,*args):
        value=self.wid_mem_non_scrolls['id_no'].text
        self.cursor.execute('''SELECT * FROM members WHERE id_no LIKE ? AND member_type="non_teacher"  ''',(value+'%',))
        rec=self.cursor.fetchall()
        rec_no=len(rec)
        
        scrolls=self.wid_mem_non_scrolls
        
        if rec_no!=0:
            recs=rec[rec_no-1]
            scrolls['id_no'].text=str(recs[3])
            scrolls['name'].text=str(recs[4])
            
            #sets the gender
            if recs[5]=='M':
                scrolls['gender_female'].active=False
                scrolls['gender_male'].active=True
            else:
                scrolls['gender_female'].active=True
                scrolls['gender_male'].active=False
                
            #load image
            req_pic='%s.jpg'%self.wid_mem_non_scrolls['id_no'].text
            
            if req_pic not in self.non_pics:
                self.img_non_teaching.img.source='pics/account.png'
            else:
                self.img_non_teaching.img.reload()
                self.img_non_teaching.img.source='non_pics/%s.jpg'%self.wid_mem_non_scrolls['id_no'].text

        else:
            scrolls['id_no'].text='No record found !'
            scrolls['name'].text=''
            self.img_non_teaching.img.source='pics\\account.png'
            
        
    ################################################ MEMBERS REGISTRATION
    #teachers and non taching stuff registration
    #clear widgets
    def clear_tan_controls(self,scrolls,*args):
        scrolls['id_no'].text=''
        scrolls['name'].text=''
        
    #Delete record for many and one
    def delete_tan(self,nav,controls,*args):
        adm=controls['id_no'].text
        name=controls['name'].text
        
        if adm !='':
            self.cursor.execute('''SELECT * FROM members WHERE id_no =?''',(adm,))
            rec=self.cursor.fetchall()
            rec_no=len(rec)

            if rec_no==0:
                opt='no'
            else:
                opt='yes'

            if opt=='yes':
                content = MDLabel(font_style='Caption',
                          text='Do you want to delete [b]%s[/b] id number [b]%s[/b] from database ?'%(name,adm), 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Member deletion !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.delete_tan_reg(adm,nav))

                self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
                                                  
                self.dialog.open()
            else:
                #dialog for invalid book accession number
                content = MDLabel(font_style='Caption',
                          text='Please enter a valid id number to delete', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Invalid id number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
                
                self.dialog.open()
                
        else:
            #dialog for blank book accession number
            content = MDLabel(font_style='Caption',
                          text='Please enter an admission number to delete', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty admission number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
            

    def delete_tan_reg(self,adm,nav,*args):
        self.dialog.dismiss()
        #check if member has ever borrowed a book
        self.cursor.execute('''SELECT book_accession_no FROM borrow WHERE id_no = ?''',(adm,))
        any_rec = self.cursor.fetchall()

        if len(any_rec) >= 1:
            content = MDLabel(font_style='Caption', text='This member has borrowed some books which needs to be returned first', \
                              size_hint=(1,None), valign='middle', halign='left', markup=True)
            
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Record Cannot be Deleted !", content=content, size_hint=(.4, None), height=(200), auto_dismiss=False)
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            
            self.cursor.execute('''DELETE FROM members WHERE id_no= ? ''',adm,)
            self.connection.commit()
            
            self.dialog.dismiss()
            
            self.show_nav_anim(nav,'pic_control/x.png',\
                                                  '[b]Record deleted successfully[/b]',2)
            
    
    #update tan record
    def update_tan_reg(self,controls,nav,*args):
        adm=controls['id_no'].text
        name=controls['name'].text

        if adm !='':
            self.cursor.execute('''SELECT * FROM members WHERE id_no =? ''',(adm,))
            rec=self.cursor.fetchall()
            rec_no=len(rec)

            if rec_no==0:
                opt='no'
            else:
                opt='yes'

            if opt=='yes':
                content = MDLabel(font_style='Caption',
                          text='Are you sure you want to update Id number [b]%s[/b] name [b]%s[/b]\
                                '%(adm,name),
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Update Record",
                               content=content,
                               size_hint=(.5, None),
                               height=(200),
                               auto_dismiss=False)
            
                self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.do_update_tan_reg(controls,nav))

                self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
            else:
                #dialog for valid book accession number
                content = MDLabel(font_style='Caption',
                          text='You have entered an invalid id number', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Invalid id number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
        else:
            #dialog for blank book accession number
            content = MDLabel(font_style='Caption',
                          text='Please enter an id number to update', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty id number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        

    def do_update_tan_reg(self,controls,nav,*args):
        id_no=controls['id_no'].text
        name=controls['name'].text
        
        if controls['gender_female'].active==True:
            gender='F'
        elif controls['gender_male'].active==True:
            gender='M'

        self.cursor.execute('''UPDATE members SET id_no=?, name=?,\
                                 gender=? WHERE id_no=? ''',\
                                    (id_no,name,gender,id_no,))
        self.connection.commit()

        self.dialog.dismiss()
        self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Record updated successfully [/b]',2)
        

        
    def move_to_first_record_tan(self,controls,nav,index_no,index_name,ton,*args):
            
        if ton=='t':
            member_type='teacher'
        else:
            member_type='non_teacher'
            
        self.cursor.execute('''SELECT * FROM members WHERE member_type=? ORDER BY id ASC LIMIT 1''',(member_type,))
        rec=self.cursor.fetchall()        
    
        lis=rec
        
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the first record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])
        
            #sets the gender
            if recs[5]=='M':
                controls['gender_female'].active=False
                controls['gender_male'].active=True
            else:
                controls['gender_female'].active=True
                controls['gender_male'].active=False
                
                
            if ton=='t':
                self.index_teach_reg=recs[0]
                file=open('index_teach_reg.txt','w')
                file.write(str(self.index_teach_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers.img.source='pics\\account.png'
                else:
                    self.img_teachers.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers.img.reload()
            else:
                self.index_non_reg=recs[0]
                file=open('index_non_reg.txt','w')
                file.write(str(self.index_non_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching.img.source='pics\\account.png'
                else:
                    self.img_non_teaching.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching.img.reload()
                

        
    def move_to_last_record_tan(self,controls,nav,index_no,index_name,ton,*args):
        if ton=='t':
            member_type='teacher'
        else:
            member_type='non_teacher'
            
        self.cursor.execute('''SELECT * FROM members WHERE member_type=? ORDER BY id DESC LIMIT 1''',(member_type,))
        rec=self.cursor.fetchall()        

        lis=rec
        
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])

            #sets the gender
            if recs[5]=='M':
                controls['gender_female'].active=False
                controls['gender_male'].active=True
            else:
                controls['gender_female'].active=True
                controls['gender_male'].active=False
                
            #get the number of all records and assign the index
            self.cursor.execute('''SELECT * FROM members''')
            rec=self.cursor.fetchall()
            rec_no=len(rec)

            if ton=='t':
                self.index_teach_reg=recs[0]
                file=open('index_teach_reg.txt','w')
                file.write(str(self.index_teach_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers.img.source='pics\\account.png'
                else:
                    self.img_teachers.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers.img.reload()
            else:
                self.index_non_reg=recs[0]
                file=open('index_non_reg.txt','w')
                file.write(str(self.index_non_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching.img.source='pics\\account.png'
                else:
                    self.img_non_teaching.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching.img.reload()
                    

    def move_to_prev_record_tan(self,controls,nav,index_no,ton,*args):
        if ton=='t':
            self.cursor.execute('''SELECT * FROM members WHERE id < ? AND member_type="teacher" ORDER BY id DESC LIMIT 1''',(self.index_teach_reg,))
        elif ton=='n':
            self.cursor.execute('''SELECT * FROM members WHERE id < ? AND member_type="non_teacher" ORDER BY id DESC LIMIT 1''',(self.index_non_reg,))

        rec=self.cursor.fetchall()        

        lis=rec
               
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the first record !  [/b]',1)
        else:
            recs=lis[0]
        
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])

            #sets the gender
            if recs[5]=='M':
                controls['gender_female'].active=False
                controls['gender_male'].active=True
            else:
                controls['gender_female'].active=True
                controls['gender_male'].active=False
                
            if ton=='t':
                self.index_teach_reg=recs[0]
                file=open('index_teach_reg.txt','w')
                file.write(str(self.index_teach_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers.img.source='pics\\account.png'
                else:
                    self.img_teachers.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers.img.reload()
            else:
                self.index_non_reg=recs[0]
                file=open('index_non_reg.txt','w')
                file.write(str(self.index_non_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching.img.source='pics\\account.png'
                else:
                    self.img_non_teaching.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching.img.reload()
                    
            
    def move_to_next_record_tan(self,controls,nav,index_no,ton,*args):
        if ton=='t':
            self.cursor.execute('''SELECT * FROM members WHERE id > ? AND member_type="teacher" ORDER BY id ASC LIMIT 1''',(self.index_teach_reg,))
        elif ton=='n':
            self.cursor.execute('''SELECT * FROM members WHERE id > ? AND member_type="non_teacher" ORDER BY id ASC LIMIT 1''',(self.index_non_reg,))
            
        rec=self.cursor.fetchall()        
        lis=rec

        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])

            #sets the gender
            if recs[5]=='M':
                controls['gender_female'].active=False
                controls['gender_male'].active=True
            else:
                controls['gender_female'].active=True
                controls['gender_male'].active=False
                

            if ton=='t':
                self.index_teach_reg=recs[0]
                file=open('index_teach_reg.txt','w')
                file.write(str(self.index_teach_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.teach_pics:
                    self.img_teachers.img.source='pics\\account.png'
                else:
                    self.img_teachers.img.source='teach_pic\\%s.jpg'%controls['id_no'].text
                    self.img_teachers.img.reload()
            else:
                self.index_non_reg=recs[0]
                file=open('index_non_reg.txt','w')
                file.write(str(self.index_non_reg))
                file.close()

                #load image
                req_pic='%s.jpg'%controls['id_no'].text
            
                if req_pic not in self.non_pics:
                    self.img_non_teaching.img.source='pics\\account.png'
                else:
                    self.img_non_teaching.img.source='non_pics\\%s.jpg'%controls['id_no'].text
                    self.img_non_teaching.img.reload()
                    

    def add_member_tan(self,controls,nav,inputs,ton,*args):
        #sets the gender
        if controls['gender_female'].active==True:
            gender='F'
        elif controls['gender_male'].active==True:
            gender='M'

        continu='yes'
        for cont in controls.values():
            if isinstance(cont,TextInput):
                if len(cont.text)==0:
                    continu='no'
        
                
        if continu=='yes':

            id_no=controls['id_no'].text
            name=controls['name'].text

            if ton=='t':
                member_type='teacher'
            else:
                member_type='non_teacher'

            #ensure there is no duplicate in adm no
            self.cursor.execute(''' SELECT id_no FROM members''')
            dp_id_chk=self.cursor.fetchall()
            
            duplicted='no'
            for cont in dp_id_chk:
                if id_no==cont[0]:
                    duplicted='yes'
                
            if duplicted=='yes':
                self.show_nav_anim(nav,'pics\\noti_error.png',\
                                                  '[b]Duplicate Id number[/b] [i]record not added successfuly[/i]',2,inputs)
            else:
                self.cursor.execute('''INSERT INTO members(id_no,name,gender,member_type)\
                                                    VALUES(?,?,?,?)''',(id_no,name,gender,member_type,))
                self.backup_counter+=1
                #save the backup_counter
                a=open('backup_counter.txt','w')
                a.write(str(self.backup_counter))
                a.close()
                self.show_nav_anim(nav,'pic_control\\tick.png',\
                                                  '[b]Record added successfully [/b]',2,inputs)

            #clear contents for new data
            controls['id_no'].text=''
            controls['name'].text=''
            
            try:
                self.connection.commit()
            except:
                pass
        else:
             self.show_nav_anim(nav,'pics\\noti_error.png',\
                                                  '[b]You are required to fill every field [/b]',3)
             
    
    #students registration
    #clear widgets
    def clear_std_controls(self,scrolls,*args):
        scrolls['adm_no'].text=''
        scrolls['clas'].text=''
        scrolls['id_no'].text=''
        scrolls['name'].text=''
        self.img_std.img.source='pics\\account.png'
        
    #Delete record for many and one
    def delete_std(self,*args):
        adm=self.wid_mem_std_scrolls['adm_no'].text
        name=self.wid_mem_std_scrolls['name'].text
        
        if adm !='':
            self.cursor.execute('''SELECT * FROM members WHERE adm_no =?''',(adm,))
            rec=self.cursor.fetchall()
            rec_no=len(rec)

            if rec_no==0:
                opt='no'
            else:
                opt='yes'

            if opt=='yes':
                content = MDLabel(font_style='Caption',
                          text='Do you want to delete student name %s admission number %s from database ?'%(name,adm), 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Book deletion !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.delete_std_reg(adm))

                self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
                                                  
                self.dialog.open()
            else:
                #dialog for invalid book accession number
                content = MDLabel(font_style='Caption',
                          text='Please enter a valid admission number to delete', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Invalid admission number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
                
                self.dialog.open()
                
        else:
            #dialog for blank book accession number
            content = MDLabel(font_style='Caption', text='Please enter an admission number to delete', size_hint=(1,None), valign='middle', halign='left', markup=True)
            
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty admission number !", content=content, size_hint=(.4, None), height=(200), auto_dismiss=False)
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
            

    def delete_std_reg(self,adm,*args):
        self.dialog.dismiss()
        #check if student has ever borrowed a book
        self.cursor.execute('''SELECT book_accession_no FROM borrow WHERE adm_no = ?''',(adm,))
        any_rec = self.cursor.fetchall()

        if len(any_rec) >= 1:
            content = MDLabel(font_style='Caption', text='This student has borrowed some books which needs to be returned first', \
                              size_hint=(1,None), valign='middle', halign='left', markup=True)
            
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Record Cannot be Deleted !", content=content, size_hint=(.4, None), height=(200), auto_dismiss=False)
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            
            self.cursor.execute('''DELETE FROM members WHERE adm_no= ? ''',(adm,))
            self.connection.commit()            
            self.dialog.dismiss()
            
            self.show_nav_anim(self.navigator_std,'pic_control\\x.png',\
                                                  '[b]Record deleted successfully[/b]',2)
            
    
    #update student record
    def update_std_reg(self,*args):
        adm=self.wid_mem_std_scrolls['adm_no'].text
        name=self.wid_mem_std_scrolls['name'].text

        if adm !='':
            self.cursor.execute('''SELECT * FROM members WHERE adm_no =?''',(adm,))
            rec=self.cursor.fetchall()
            rec_no=len(rec)

            if rec_no==0:
                opt='no'
            else:
                opt='yes'

            if opt=='yes':
                content = MDLabel(font_style='Caption',
                          text='Are you sure you want to update admission number [b]%s[/b] studets name [b]%s[/b]\
                                '%(adm,name),
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Update Record",
                               content=content,
                               size_hint=(.5, None),
                               height=(200),
                               auto_dismiss=False)
            
                self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.do_update_std_reg())

                self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
            else:
                #dialog for valid book accession number
                content = MDLabel(font_style='Caption',
                          text='You have entered an invalid admission number', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Invalid admission number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
        else:
            #dialog for blank book accession number
            content = MDLabel(font_style='Caption',
                          text='Please enter an admission number to update', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty admission number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        

    def do_update_std_reg(self,*args):
        adm=self.wid_mem_std_scrolls['adm_no'].text
        clas=self.wid_mem_std_scrolls['clas'].text
        id_no=self.wid_mem_std_scrolls['id_no'].text
        name=self.wid_mem_std_scrolls['name'].text
        
        if self.wid_mem_std_scrolls['gender_female'].active==True:
            gender='F'
        elif self.wid_mem_std_scrolls['gender_male'].active==True:
            gender='M'

        self.cursor.execute('''UPDATE members SET adm_no=?, class=?,id_no=?, name=?,\
                                 gender=? WHERE adm_no=? ''',\
                            (adm,clas,id_no,name,gender,adm,))

        self.connection.commit()

        self.show_nav_anim(self.navigator_std,'pics\\noti.png',\
                                                  '[b]Record updated successfully [/b]',2)
        self.dialog.dismiss()

        
    def move_to_first_record_std(self,controls,nav,*args):
        self.cursor.execute('''SELECT * FROM members WHERE member_type="student" ORDER BY id ASC LIMIT 1''')
        rec=self.cursor.fetchall()
        lis=rec
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the first record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['adm_no'].text=str(recs[1])
            controls['clas'].text=str(recs[2])
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])
        
            #sets the gender
            if recs[5]=='M':
                self.wid_mem_std_scrolls['gender_female'].active=False
                self.wid_mem_std_scrolls['gender_male'].active=True
            else:
                self.wid_mem_std_scrolls['gender_female'].active=True
                self.wid_mem_std_scrolls['gender_male'].active=False

            #load image
            req_pic='%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
            if req_pic not in self.std_pics:
                self.img_std.img.source='pics\\account.png'
            else:
                self.img_std.img.reload()
                self.img_std.img.source='std_pic\\%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            

            self.index_std_reg=1
            file=open('index_std_reg.txt','w')
            file.write(str(self.index_std_reg))
            file.close()
        
    def move_to_last_record_std(self,controls,nav,*args):
        self.cursor.execute('''SELECT * FROM members WHERE member_type="student" ORDER BY id DESC LIMIT 1''')
        rec=self.cursor.fetchall()

        lis=rec
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['adm_no'].text=str(recs[1])
            controls['clas'].text=str(recs[2])
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])

            #load image
            req_pic='%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
            if req_pic not in self.std_pics:
                self.img_std.img.source='pics\\account.png'
            else:
                self.img_std.img.reload()
                self.img_std.img.source='std_pic\\%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
              

            #sets the gender
            if recs[5]=='M':
                self.wid_mem_std_scrolls['gender_female'].active=False
                self.wid_mem_std_scrolls['gender_male'].active=True
            else:
                self.wid_mem_std_scrolls['gender_female'].active=True
                self.wid_mem_std_scrolls['gender_male'].active=False
                
            #get the number of all records and assign the index
            self.cursor.execute('''SELECT * FROM members''')
            rec=self.cursor.fetchall()
            rec_no=len(rec)
        
            self.index_std_reg=rec_no
            file=open('index_std_reg.txt','w')
            file.write(str(self.index_std_reg))
            file.close()

    def move_to_prev_record_std(self,controls,nav,*args):
        self.cursor.execute('''SELECT * FROM members WHERE id < ? AND member_type="student" ORDER BY id DESC LIMIT 1''',(self.index_std_reg,))
        rec=self.cursor.fetchall()
        
        lis=rec
        
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the first record ![/b]',1)
        else:
            recs=lis[0]
            
            controls['adm_no'].text=str(recs[1])
            controls['clas'].text=str(recs[2])
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])
            
            #load image
            req_pic='%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
            if req_pic not in self.std_pics:
                self.img_std.img.source='pics\\account.png'
            else:
                self.img_std.img.reload()
                self.img_std.img.source='std_pic\\%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
            #sets the gender
            if recs[5]=='M':
                self.wid_mem_std_scrolls['gender_female'].active=False
                self.wid_mem_std_scrolls['gender_male'].active=True
            else:
                self.wid_mem_std_scrolls['gender_female'].active=True
                self.wid_mem_std_scrolls['gender_male'].active=False
                
            
            self.index_std_reg-=1
            file=open('index_std_reg.txt','w')
            file.write(str(self.index_std_reg))
            file.close()
            
    def move_to_next_record_std(self,controls,nav,*args):
        self.cursor.execute('''SELECT * FROM members WHERE id > ? AND member_type="student" ORDER BY id ASC LIMIT 1''',(self.index_std_reg,))
        rec=self.cursor.fetchall()
        
        lis=rec
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['adm_no'].text=str(recs[1])
            controls['clas'].text=str(recs[2])
            controls['id_no'].text=str(recs[3])
            controls['name'].text=str(recs[4])

            #sets the gender
            if recs[5]=='M':
                self.wid_mem_std_scrolls['gender_female'].active=False
                self.wid_mem_std_scrolls['gender_male'].active=True
            else:
                self.wid_mem_std_scrolls['gender_female'].active=True
                self.wid_mem_std_scrolls['gender_male'].active=False
                
            #load image
            req_pic='%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
            if req_pic not in self.std_pics:
                self.img_std.img.source='pics\\account.png'
            else:
                self.img_std.img.reload()
                self.img_std.img.source='std_pic\\%s.jpg'%self.wid_mem_std_scrolls['adm_no'].text
            
            self.index_std_reg+=1
            file=open('index_std_reg.txt','w')
            file.write(str(self.index_std_reg))
            file.close()
               
    def add_member_std(self,*args):
        #sets the gender
        if self.wid_mem_std_scrolls['gender_female'].active==True:
            gender='F'
        elif self.wid_mem_std_scrolls['gender_male'].active==True:
            gender='M'

        continu='yes'
        for cont in self.wid_mem_std_scrolls.values():
            
            if isinstance(cont,TextInput):
                if len(cont.text)==0:
                    continu='no'
                
        if continu=='yes':

            #ensure there is no duplicate in adm no
            self.cursor.execute(''' SELECT adm_no FROM members WHERE member_type='student' ''')
            dp_adm_chk=self.cursor.fetchall()
            adm_no=self.wid_mem_std_scrolls['adm_no'].text

            duplicted='no'
            for cont in dp_adm_chk:
                if adm_no==cont[0]:
                    duplicted='yes'
                    
            if duplicted=='yes':
                self.show_nav_anim(self.navigator_std,'pics\\noti_error.png',\
                                                  '[b]Duplicate admission number [i]record not added successfully [/i] ![/b]',5,self.wid_mem_std_input)
            else:
                
                clas=self.wid_mem_std_scrolls['clas'].text
                id_no=self.wid_mem_std_scrolls['id_no'].text
                name=self.wid_mem_std_scrolls['name'].text
                
                self.cursor.execute('''INSERT INTO members(adm_no,class,id_no,name,gender,member_type)\
                                                    VALUES(?,?,?,?,?,?)''',(adm_no,clas,id_no,name,gender,'student',))
            
                self.show_nav_anim(self.navigator_std,'pic_control\\tick.png',\
                                                  '[b]Record added successfully [/b]',2,self.wid_mem_std_input)

                #clear contents for new data
                self.wid_mem_std_scrolls['adm_no'].text=''
                self.wid_mem_std_scrolls['clas'].text=''
                self.wid_mem_std_scrolls['id_no'].text=''
                self.wid_mem_std_scrolls['name'].text=''
            
                self.connection.commit()
                self.backup_counter+=1
                #save the backup_counter
                a=open('backup_counter.txt','w')
                a.write(str(self.backup_counter))
                a.close()
        else:
             self.show_nav_anim(self.navigator_std,'pics\\noti_error.png',\
                                                  '[b]You are required to fill every field [/b]',3)
             
    
    ################################################ BOOKS REGISTRATION
    ################################################ LOADING OF TABLE
     #animation notification

    def show_notification(self,content,duration=2):
        self.anim_notification=Animation(height=50,duration=.5)
        self.anim_notification.start(self.ids.box_notify)
        nfb=NotifyButton()
        nfb.ids.lbl_not.text=content
        nfb.ids.img_s.source='pics\\noti.png'
        self.ids.box_notify.add_widget(nfb)
        Clock.schedule_once(self.unshow_notification,duration)

    def unshow_notification(self,*args):
        self.anim_notification=Animation(height=0,duration=.5)
        self.anim_notification.start(self.ids.box_notify)
        self.ids.box_notify.clear_widgets()

        
    #Load records
    def load_recs_to_books_table(self):
        self.cursor.execute('''SELECT * FROM books''')
        rec=self.cursor.fetchall()
        self.table_books.recv_add.data=[]
        wg = 'g'
        for row in rec:
            counter_column=0
            if wg == 'w':
                wg ='g'
            elif wg == 'g':
                wg = 'w'
            for cols in range(len(row)-1):
                self.table_books.recv_add.data.append({'text':str(row[counter_column]), 'wg':wg})
                counter_column+=1
        

    def apply_changes(self, who):
        
        if who == 's':
            self.times_borrowed[0]=int(self.ids.txt_b_std.text)
            content = MDLabel(font_style='Caption',
                          text="The maximum books to be issued to students is [b]%s[/b] book(s) from now"%self.times_borrowed[0], 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            
        elif who =='t':
            self.times_borrowed[1]=int(self.ids.txt_b_tch.text)
            content = MDLabel(font_style='Caption',
                          text="The maximum books to be issued to teachers is [b]%s[/b] book(s) from now"%self.times_borrowed[1],
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            
        elif who =='nt':
            self.times_borrowed[2]=int(self.ids.txt_b_nontch.text)

            content = MDLabel(font_style='Caption',
                          text="The maximum books to be issued to Non teaching stuff is [b]%s[/b] book(s) from now"%self.times_borrowed[2], 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))

        
        file=open('times_borrowed.txt','w')
        file.write(str(self.times_borrowed))
        file.close()

        self.dialog = MDDialog(title="Book issuing changes made",
                                content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=True)

        self.dialog.add_action_button("OK",
                                      action=lambda *x: self.dialog.dismiss())

        self.dialog.open()
        
            
    #checks if a data return results yes or no
    def check_for_valid_acc_n(self,table,acc_n):
        self.cursor.execute('''SELECT * FROM {} WHERE book_accession_no =?'''.format(table.replace('"','""')),(acc_n,))
        rec=self.cursor.fetchall()
        rec_no=len(rec)

        if rec_no==0:
            return 'no'
        else:
            return 'yes'
        
    #Clear contents
    def clear_content_for_scroll(self,scroll_wid,*args):
        scroll_wid['isbn'].text=''
        scroll_wid['tit'].text=''
        scroll_wid['pubr'].text=''
        scroll_wid['edition'].text=''
        scroll_wid['auth'].text=''
        scroll_wid['pob'].text=''
        scroll_wid['yop'].text=''
        scroll_wid['categ'].text=''
        scroll_wid['shelve'].text=''

    def show_delete_range_popup(self,nav,scroll_wid, *args):
        self.deletebubble = Deletedialog()
        self.deletebubble.ids.deleteall.bind(on_press=partial(self.delete_one_book,nav,scroll_wid, 'No'))
        self.deletebubble.ids.delete_Range.bind(on_press=partial(self.go_on_delete_range,nav,scroll_wid))

        self.viewmodal = ModalView(auto_dismiss=True, \
                                   size_hint=(None, None),\
                                   size=(dp(272), dp(181)),\
                                   pos=self.many_book_nav_buttons['update'].pos,\
                                   background = '', background_color = (0,0,0,.3),\
                                   )
        self.viewmodal.add_widget(self.deletebubble)
        self.viewmodal.open()

        self.deletebubble.ids.btnclose.bind(on_release=lambda *x:  self.viewmodal.dismiss())

    def go_on_delete_range(self,nav,scroll_wid, *args):
        #ensure the number is in range
        if self.deletebubble.ids.lblfrom.text == '' or self.deletebubble.ids.lblto.text == '':
            content = MDLabel(font_style='Caption',
                      text='Ensure every Field is filled!',
                      size_hint=(1,None),
                      valign='middle',
                      halign='left',
                      markup=True)

            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Blank fields",
                           content=content,
                           size_hint=(.5, None),
                           height=(200),
                           auto_dismiss=False)

            self.dialog.add_action_button("Ok",
                                  action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            self.delete_one_book(nav,scroll_wid,'yes')
            
    #Delete record for many and one
    def delete_one_book(self,nav,scroll_wid,rangef='No',*args):
        self.backup_manaully()
        acc_n=scroll_wid['acc_n'].text
        titl=scroll_wid['tit'].text
        if acc_n !='':
            opt=self.check_for_valid_acc_n('books',acc_n)
            if opt=='yes':

                if rangef=='No':
                    txt = 'Do you want to delete book accession number %s book title %s ?'%(acc_n,titl)
                else:
                    txt = 'Do you want to delete book accession number %s book title %s ? from accession no range %s - %s'%(acc_n,titl,\
                                                                                                                            self.deletebubble.ids.lblfrom.text,\
                                                                                                                            self.deletebubble.ids.lblto.text)
                    
                content = MDLabel(font_style='Caption',
                          text=txt, 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Book deletion !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                if rangef=='No':
                    self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.delete_book(nav,scroll_wid,acc_n))
                else:
                    self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.delete_range_book(nav,scroll_wid,acc_n))
                    

                self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
                                                  
                self.dialog.open()
            else:
                
                
                self.dialog.open()
                
        else:
            #dialog for blank book accession number
            content = MDLabel(font_style='Caption',
                          text='Please enter the accession number to delete', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty accession number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()

    def delete_range_book(self,nav,scroll_wid,acc_n,*args):
        self.dialog.dismiss()
        
        self.progressbar_load=ProgressBar()
        self.progressbar_load.value = int(self.deletebubble.ids.lblfrom.text)
        self.progressbar_load.max= int(self.deletebubble.ids.lblto.text)
        
        content =self.progressbar_load
        
        self.dialog = MDDialog(title="Deleting accession no (%s) - (%s)"%(int(self.progressbar_load.value),int(self.progressbar_load.max)),
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
        self.dialog.open()
        self.counter=int(self.deletebubble.ids.lblfrom.text)
        

        #check if book is borrowed
        self.cursor.execute('''SELECT book_accession_no FROM borrow ''')
        self.list_book_acc_no =  self.cursor.fetchall()
        self.list_borrowe_books = ''
        self.book_borrowed= 'No'
        
        Clock.schedule_interval(partial(self.one_by_one_delete_range,nav,scroll_wid,acc_n ),0)

    def one_by_one_delete_range(self,nav,scroll_wid,acc_n,*args):
        if int(self.counter) < int(self.progressbar_load.max)+1:
            self.dialog.title="Deleting records   %s/%s"%(int(self.progressbar_load.value),int(self.progressbar_load.max))
            print(self.progressbar_load.value, '/',  int(self.progressbar_load.max)+1)

            borrowed = 'No'
            for accNo in self.list_book_acc_no:
                if int(self.counter) == int(accNo[0]):
                    self.book_borrowed='yes'
                    borrowed = 'yes'
                    #fetch id/adm_no for who borrowed the book
                    self.cursor.execute(''' SELECT member_type,adm_no,id_no FROM borrow WHERE book_accession_no = ?''',(self.counter,))
                    details = self.cursor.fetchall()[0]
                    
                    self.list_borrowe_books += 'Accession no: %s member type: %s adm no: %s id no: %s \n'%(self.counter, details[0],details[1], details[2])

            if borrowed=='No':
                self.cursor.execute('''DELETE FROM books WHERE book_accession_no= ? ''',(self.counter,))
                self.connection.commit()
            
            
            self.counter+=1
            self.progressbar_load.value+=1
        else:
            self.dialog.dismiss()
            self.viewmodal.dismiss()

            if self.book_borrowed=='yes':
                #dialog for invalid book accession number
                content = MDLabel(font_style='Caption',
                          text='%s'%self.list_borrowe_books, 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)

                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="The following books were not deleted because they are borrowed:",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                self.dialog.open()

                self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            else:
                self.show_nav_anim(nav,'pic_control\\x.png',\
                                                      '[b]Record deleted successfully[/b]',2)
            
            return False

    def delete_book(self,nav,scroll_wid,acc_n,*args):
        self.dialog.dismiss()
        #check if book is borrowed
        self.cursor.execute('''SELECT book_accession_no FROM borrow ''')
        book_acc_no =  self.cursor.fetchall()

        book_brrw='No'  
        for accNo in book_acc_no:
            if acc_n == accNo[0]:
                book_brrw='yes'

            
        if book_brrw == 'No':
            self.cursor.execute('''DELETE FROM books WHERE book_accession_no= ? ''',(acc_n,))
            self.connection.commit()

            self.show_nav_anim(nav,'pic_control\\x.png',\
                                                  '[b]Record deleted successfully[/b]',2)
        else:
            #fetch id/adm_no for who borrowed the book
            self.cursor.execute(''' SELECT member_type,adm_no,id_no FROM borrow WHERE book_accession_no = ?''',(acc_n,))
            details = self.cursor.fetchall()[0]
            
            #dialog for invalid book accession number
            content = MDLabel(font_style='Caption',
                      text='This book is already borrowed by member type %s adm no %s id no %s'%(details[0],details[1], details[2]), 
                      size_hint=(1,None),
                      valign='middle',
                      halign='left',
                      markup=True)

            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Error deleting",
                               content=content,
                           size_hint=(.4, None),
                           height=(200),
                           auto_dismiss=False)
            self.dialog.open()
            
            self.dialog.add_action_button("Ok",
                                  action=lambda *x: self.dialog.dismiss())
        
        
        
        
            
    def show_update_range_popup(self, *args):
        self.updatebubble = Updatedialog()
        self.updatebubble.ids.updateall.bind(on_press=partial(self.update_once_many_book, 'No'))
        self.updatebubble.ids.update_Range.bind(on_press=partial(self.go_on_update_range))

        self.viewmodal = ModalView(auto_dismiss=True, \
                                   size_hint=(None, None),\
                                   size=(dp(272), dp(181)),\
                                   pos=self.many_book_nav_buttons['update'].pos,\
                                   background = '', background_color = (0,0,0,.3),\
                                   )
        self.viewmodal.add_widget(self.updatebubble)
        self.viewmodal.open()

        self.updatebubble.ids.btnclose.bind(on_release=lambda *x:  self.viewmodal.dismiss())

    def go_on_update_range(self, *args):
        self.cursor.execute(''' SELECT COUNT(*) FROM books ''')
        no =self.cursor.fetchall()[0][0]
        #ensure the number is in range
        if self.updatebubble.ids.lblfrom.text == '' or self.updatebubble.ids.lblto.text == '':
            content = MDLabel(font_style='Caption',
                      text='Ensure every Field is filled!',
                      size_hint=(1,None),
                      valign='middle',
                      halign='left',
                      markup=True)

            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Blank fields",
                           content=content,
                           size_hint=(.5, None),
                           height=(200),
                           auto_dismiss=False)

            self.dialog.add_action_button("Ok",
                                  action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
        else:
            self.update_once_many_book(ranget='yes')
    
    #update a record
    def update_once_many_book(self,ranget='No',*args):
        self.backup_manaully()
        acc_n=self.many_book_scroll_inputs['acc_n'].text

        self.cursor.execute(''' SELECT title FROM books WHERE book_accession_no= ? ''',(acc_n,))
        tit=self.cursor.fetchall()
        
        
        if acc_n !='':
            opt=self.check_for_valid_acc_n('books',acc_n)

            if opt=='yes':
                print(ranget, 'ranget')
                if ranget=='No':
                    txt = 'This will update all existing books with the title [b]%s[/b] to [b]%s[/b]\
                                '%(tit[0][0], self.many_book_scroll_inputs['tit'].text)
                else:
                    txt = 'This will update all existing books with the title [b]%s[/b] to [b]%s[/b] from accession no %s - %s\
                                '%(tit[0][0], self.many_book_scroll_inputs['tit'].text, self.updatebubble.ids.lblfrom.text, self.updatebubble.ids.lblto.text)
                    
                content = MDLabel(font_style='Caption',
                          text=txt,
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Update Record",
                               content=content,
                               size_hint=(.5, None),
                               height=(200),
                               auto_dismiss=False)

                if ranget=='No':
                    self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.do_update_many())
                else:
                    self.dialog.add_action_button("Yes",
                                          action=lambda *x: self.do_update_many_range())

                self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
                    
            else:
                #dialog for valid book accession number
                content = MDLabel(font_style='Caption',
                          text='You have entered an invalid book accession number', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Invalid book accession number",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
        else:
            #dialog for blank book accession number
            content = MDLabel(font_style='Caption',
                          text='Please enter the accession number to update', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty accession number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()

    def do_update_many_range(self,*args):
        self.dialog.dismiss()
        
        self.progressbar_load=ProgressBar()
        self.progressbar_load.value = int(self.updatebubble.ids.lblfrom.text)
        self.progressbar_load.max= int(self.updatebubble.ids.lblto.text)
        
        content =self.progressbar_load
        
        self.dialog = MDDialog(title="Updating accession no (%s) - (%s)"%(int(self.progressbar_load.value),int(self.progressbar_load.max)),
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
        self.dialog.open()
        self.counter=int(self.updatebubble.ids.lblfrom.text)
        
        Clock.schedule_interval(self.one_by_one_update_range,0)

    def one_by_one_update_range(self,*args):
        if self.progressbar_load.value+1 < self.progressbar_load.max:
            self.dialog.title="Updating records   %s/%s"%(int(self.progressbar_load.value+1),int(self.progressbar_load.max))
            acc_n=self.counter
            titl=self.many_book_scroll_inputs['tit'].text
            isbn=self.many_book_scroll_inputs['isbn'].text
            tit=self.many_book_scroll_inputs['tit'].text
            pubr=self.many_book_scroll_inputs['pubr'].text
            editn=self.many_book_scroll_inputs['edition'].text
            auth=self.many_book_scroll_inputs['auth'].text
            pob=self.many_book_scroll_inputs['pob'].text
            yop=self.many_book_scroll_inputs['yop'].text
            categ=self.many_book_scroll_inputs['categ'].text
            shelve_no=self.many_book_scroll_inputs['shelve'].text

            self.cursor.execute('''UPDATE books SET isbn=?, title=?,publisher=?, edition=?,\
                                 author=?, place_of_publication=?,\
                                 year_of_publication=? , category=?,\
                                 shelve_no=? WHERE book_accession_no=? ''',\
                            (isbn,tit,pubr,editn,auth,pob,yop,categ,shelve_no,acc_n,))

            self.connection.commit()
            
            self.counter+=1
            self.progressbar_load.value+=1
        else:
            self.dialog.dismiss()
            self.viewmodal.dismiss()
            self.show_nav_anim(self.nav_books_many,'pics\\noti.png',\
                                                  '[b]Record updated successfully [/b]',2)
            
            return False

    def do_update_many(self,*args):
        self.dialog.dismiss()
        acc_n=self.many_book_scroll_inputs['acc_n'].text
        
        #select the book title of the book before the update from database not from the form
        self.cursor.execute('''SELECT title FROM books WHERE book_accession_no= ? ''',(acc_n,))
        self.titl=self.cursor.fetchall()
        #get the record length for loading
        self.cursor.execute(''' SELECT book_accession_no FROM books WHERE title=? ''',(str(self.titl[0][0]),))
        self.rec=self.cursor.fetchall()
        rec_no=len(self.rec)
        self.progressbar_load=ProgressBar()
        self.progressbar_load.max=rec_no
        content =self.progressbar_load
        
        self.dialog = MDDialog(title="Updating records (%s)/(%s)"%(int(self.progressbar_load.value),int(self.progressbar_load.max)),
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
        self.dialog.open()
        self.counter=0
        
        Clock.schedule_interval(self.one_by_one_update,0)

    def one_by_one_update(self,*args):
        if self.progressbar_load.value < self.progressbar_load.max:
            self.dialog.title="Updating records   %s/%s"%(int(self.progressbar_load.value+1),int(self.progressbar_load.max))
            acc_n=self.rec[self.counter]
            titl=self.titl
            isbn=self.many_book_scroll_inputs['isbn'].text
            tit=self.many_book_scroll_inputs['tit'].text
            pubr=self.many_book_scroll_inputs['pubr'].text
            editn=self.many_book_scroll_inputs['edition'].text
            auth=self.many_book_scroll_inputs['auth'].text
            pob=self.many_book_scroll_inputs['pob'].text
            yop=self.many_book_scroll_inputs['yop'].text
            categ=self.many_book_scroll_inputs['categ'].text
            shelve_no=self.many_book_scroll_inputs['shelve'].text

            self.cursor.execute('''UPDATE books SET isbn=?, title=?,publisher=?, edition=?,\
                                 author=?, place_of_publication=?,\
                                 year_of_publication=? , category=?,\
                                 shelve_no=? WHERE book_accession_no=? ''',\
                            (isbn,tit,pubr,editn,auth,pob,yop,categ,shelve_no,acc_n[0],))

            self.connection.commit()
            
            self.counter+=1
            self.progressbar_load.value+=1
        else:
            self.dialog.dismiss()
            self.viewmodal.dismiss()
            self.show_nav_anim(self.nav_books_many,'pics\\noti.png',\
                                                  '[b]Record updated successfully [/b]',2)
            
            return False
    
    #update a record
    def update_once_one_book(self,*args):
        acc_n=self.one_book_scroll_inputs['acc_n'].text
        tit=self.one_book_scroll_inputs['tit'].text

        if acc_n !='':
            opt=self.check_for_valid_acc_n('books',acc_n)

            if opt=='yes':
                content = MDLabel(font_style='Caption',
                          text='Are you sure you want to update book title [b]%s[/b] book accession number [b]%s[/b]\
                                '%(tit,acc_n),
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Update Record",
                               content=content,
                               size_hint=(.5, None),
                               height=(200),
                               auto_dismiss=False)
            
                self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.do_update())

                self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
            else:
                #dialog for valid book accession number
                content = MDLabel(font_style='Caption',
                          text='You have entered an invalid book accession number', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
                content.bind(texture_size=content.setter('size'))
                self.dialog = MDDialog(title="Invalid book accession number",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
                self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
                self.dialog.open()
        else:
            #dialog for blank book accession number
            content = MDLabel(font_style='Caption',
                          text='Please enter the accession number to update', 
                          size_hint=(1,None),
                          valign='middle',
                          halign='left',
                          markup=True)
    
            content.bind(texture_size=content.setter('size'))
            self.dialog = MDDialog(title="Empty accession number !",
                                   content=content,
                               size_hint=(.4, None),
                               height=(200),
                               auto_dismiss=False)
                
            self.dialog.add_action_button("Ok",
                                      action=lambda *x: self.dialog.dismiss())
            self.dialog.open()
                
            
        

    def do_update(self,*args):
        acc_n=self.one_book_scroll_inputs['acc_n'].text
        isbn=self.one_book_scroll_inputs['isbn'].text
        tit=self.one_book_scroll_inputs['tit'].text
        pubr=self.one_book_scroll_inputs['pubr'].text
        editn=self.one_book_scroll_inputs['edition'].text
        auth=self.one_book_scroll_inputs['auth'].text
        pob=self.one_book_scroll_inputs['pob'].text
        yop=self.one_book_scroll_inputs['yop'].text
        categ=self.one_book_scroll_inputs['categ'].text
        shelve_no=self.one_book_scroll_inputs['shelve'].text

        self.cursor.execute('''UPDATE books SET isbn=?, title=?,publisher=?, edition=?,\
                                 author=?, place_of_publication=?,\
                                 year_of_publication=? , category=?,\
                                 shelve_no=? WHERE book_accession_no=? ''',\
                            (isbn,tit,pubr,editn,auth,pob,yop,categ,shelve_no,acc_n,))
        self.connection.commit()

        self.show_nav_anim(self.nav_books,'pics\\noti.png',\
                                                  '[b]Record updated successfully [/b]',2)
        self.dialog.dismiss()

    def change_state_toolbar(self,value):
        
        if value == 'normal':
            self.ids.contH1.state = 'normal'
            self.ids.contH2.state = 'normal'
            self.ids.contH3.state = 'normal'
            self.ids.contH4.state = 'normal'
            self.ids.contH5.state = 'normal'
            self.ids.contH6.state = 'normal'
            self.ids.contH7.state = 'normal'
        
    def add_one_book_record(self,*args):
        #calculate the next id number
        self.cursor.execute(''' SELECT book_accession_no FROM books ''')
        rec=self.cursor.fetchall()
        last_rec_no=len(rec)
        if last_rec_no==0:
            rec_no=1
        else:
            rec_no=rec[last_rec_no-1][0]
            rec_no+=1
        
        #adds 'empty' to blank fields
        for content in self.one_book_scroll_inputs.values():
            if content.text=='':
                content.text='empty'
        
        #enter content into variables
        idd=rec_no
        isbn=self.one_book_scroll_inputs['isbn'].text
        tit=self.one_book_scroll_inputs['tit'].text
        pubr=self.one_book_scroll_inputs['pubr'].text
        editn=self.one_book_scroll_inputs['edition'].text
        auth=self.one_book_scroll_inputs['auth'].text
        pob=self.one_book_scroll_inputs['pob'].text
        yop=self.one_book_scroll_inputs['yop'].text
        categ=self.one_book_scroll_inputs['categ'].text
        shelve_no=self.one_book_scroll_inputs['shelve'].text
        user=self.user_name

        self.cursor.execute('''INSERT INTO books(isbn,title,publisher,edition,author,place_of_publication,year_of_publication,category,\
                                                    shelve_no,by_user,id, lost, lost_by, borrowed, borrowed_by,damaged,damaged_by)\
                                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',\
                            (isbn,tit,pubr,editn,auth,pob,yop,categ,shelve_no,user,idd, 'no', 'none', 'no', 'none', 'no', 'none',))
        
        self.show_nav_anim(self.nav_books,'pic_control\\tick.png',\
                                            '[b]Record added succesfully [/b]',2,self.one_book_nav_buttons)
        self.connection.commit()
        self.backup_counter+=1
        #save the backup_counter
        a=open('backup_counter.txt','w')
        a.write(str(self.backup_counter))
        a.close()
                                                 
        #clear contents for new data
        self.one_book_scroll_inputs['isbn'].text=''
        self.one_book_scroll_inputs['tit'].text=''
        self.one_book_scroll_inputs['pubr'].text=''
        self.one_book_scroll_inputs['edition'].text=''
        self.one_book_scroll_inputs['auth'].text=''
        self.one_book_scroll_inputs['pob'].text=''
        self.one_book_scroll_inputs['yop'].text=''
        self.one_book_scroll_inputs['categ'].text=''
        self.one_book_scroll_inputs['shelve'].text=''

            
    def add_many_book_record(self,*args):
        # calculate the next id number
        self.cursor.execute(''' SELECT * FROM books ''')
        rec=self.cursor.fetchall()
        rec_no=len(rec)

        self.book_q=self.many_book_scroll_inputs['book_q'].text
        if self.book_q =='':
            self.book_q=0

        self.new_acc=int(rec_no)+int(self.book_q)
        
        content = MDLabel(font_style='Body2',
                          text='The number of books to be added is %s and the last book accession number will be %s do you want\
                                to procees '%(self.book_q,self.new_acc),
                          size_hint=(1,None),
                          valign='middle',
                          halign='left')

        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Mass book addition",
                               content=content,
                               size_hint=(.5, None),
                               height=(200),
                               auto_dismiss=False)
        
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.show_loading())

        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
        
    def show_loading(self):
        self.dialog.dismiss()
        #loading progressbar
        self.progress_many=ProgressBar(size_hint=(1,1))
        self.progress_many.max=self.book_q
        
        #label for showing progress
        Box_l=BoxLayout(orientation='vertical',size_hint=(1,1))
        self.loading_lbl=MDLabel(halign='center',size_hint=(1,.5))
        Box_l.add_widget(self.loading_lbl)
        Box_l.add_widget(self.progress_many)
        
        content = Box_l
        self.dialog_load = MDDialog(title="Adding records please wait...",
                               content=content,
                               size_hint=(.5, None),
                               height=(200),
                               auto_dismiss=False)
        self.dialog_load.open()
        
        Clock.schedule_interval(self.add,0)
        
    def add(self,*args):
        self.dialog_load.title='Adding records please wait... (%s/%s)'%(int(self.progress_many.value),int(self.progress_many.max))
        if self.progress_many.value < self.progress_many.max:
            # adds 'empty' to blank fields
            for content in self.many_book_scroll_inputs.values():
                if content.text=='':
                    content.text='empty'
            
        
            #calculate the next id number
            self.cursor.execute(''' SELECT book_accession_no FROM books ''')
            rec=self.cursor.fetchall()
            last_rec_no=len(rec)
            if last_rec_no==0:
                rec_no=1
            else:
                rec_no=rec[last_rec_no-1][0]
                rec_no+=1

            #enter content into variables
            idd=rec_no
            isbn=self.many_book_scroll_inputs['isbn'].text
            tit=self.many_book_scroll_inputs['tit'].text
            pubr=self.many_book_scroll_inputs['pubr'].text
            editn=self.many_book_scroll_inputs['edition'].text
            auth=self.many_book_scroll_inputs['auth'].text
            pob=self.many_book_scroll_inputs['pob'].text
            yop=self.many_book_scroll_inputs['yop'].text
            categ=self.many_book_scroll_inputs['categ'].text
            shelve_no=self.many_book_scroll_inputs['shelve'].text
            user=self.user_name
            
            self.cursor.execute('''INSERT INTO books(isbn,title,publisher,edition,author,place_of_publication,year_of_publication,category,\
                                                    shelve_no,by_user,id, lost, lost_by, borrowed, borrowed_by, damaged, damaged_by)\
                                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',\
                                (isbn,tit,pubr,editn,auth,pob,yop,categ,shelve_no,user,idd, 'no', 'none', 'no', 'none', 'no', 'none',))
         
            self.connection.commit()
            self.progress_many.value+=1
            
        elif self.progress_many.value==self.progress_many.max:
            self.dialog_load.dismiss()
            #clear contents for new data
            self.many_book_scroll_inputs['isbn'].text=''
            self.many_book_scroll_inputs['tit'].text=''
            self.many_book_scroll_inputs['pubr'].text=''
            self.many_book_scroll_inputs['edition'].text=''
            self.many_book_scroll_inputs['auth'].text=''
            self.many_book_scroll_inputs['pob'].text=''
            self.many_book_scroll_inputs['yop'].text=''
            self.many_book_scroll_inputs['categ'].text=''
            self.many_book_scroll_inputs['shelve'].text=''
            self.backup_counter+=20
            #save the backup_counter
            a=open('backup_counter.txt','w')
            a.write(str(self.backup_counter))
            a.close()
            self.show_nav_anim(self.nav_books_many,'pic_control\\tick.png',\
                                    '[b]Record added succesfully [/b]',2,self.many_book_nav_buttons)
            return False

    def move_to_first_record_books(self,controls,nav,*args):
        self.index_books_reg=1
        lis=self.move_to_first_record_one_book('books')
        
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the first record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['acc_n'].text=str(recs[0])
            controls['isbn'].text=str(recs[2])
            controls['tit'].text=str(recs[3])
            controls['pubr'].text=str(recs[4])
            controls['edition'].text=str(recs[5])
            controls['auth'].text=str(recs[6])
            controls['pob'].text=str(recs[7])
            controls['yop'].text=str(recs[8])
            controls['categ'].text=str(recs[9])
            controls['shelve'].text=str(recs[10])
        
        
            file=open('index_books_reg.txt','w')
            file.write(str(self.index_books_reg))
            file.close()

        
    def move_to_last_record_books(self,controls,nav,*args):
        lis=self.move_to_last_record_one_book('books')
        
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['acc_n'].text=str(recs[0])
            controls['isbn'].text=str(recs[2])
            controls['tit'].text=str(recs[3])
            controls['pubr'].text=str(recs[4])
            controls['edition'].text=str(recs[5])
            controls['auth'].text=str(recs[6])
            controls['pob'].text=str(recs[7])
            controls['yop'].text=str(recs[8])
            controls['categ'].text=str(recs[9])
            controls['shelve'].text=str(recs[10])

            #get the number of all records and assign the index
            self.cursor.execute('''SELECT * FROM books ''')
            rec=self.cursor.fetchall()
            rec_no=len(rec)
        
            self.index_books_reg=rec_no
            file=open('index_books_reg.txt','w')
            file.write(str(self.index_books_reg))
            file.close()

    def move_to_next_record_books(self,controls,nav,*args):
        lis=self.move_to_next_record_one_book('books',self.index_books_reg)
        
        
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the last record ! [/b]',1)
        else:
            recs=lis[0]
        
            controls['acc_n'].text=str(recs[0])
            controls['isbn'].text=str(recs[2])
            controls['tit'].text=str(recs[3])
            controls['pubr'].text=str(recs[4])
            controls['edition'].text=str(recs[5])
            controls['auth'].text=str(recs[6])
            controls['pob'].text=str(recs[7])
            controls['yop'].text=str(recs[8])
            controls['categ'].text=str(recs[9])
            controls['shelve'].text=str(recs[10])

            self.index_books_reg+=1
            file=open('index_books_reg.txt','w')
            file.write(str(self.index_books_reg))
            file.close()
        

    def move_to_prev_record_books(self,controls,nav,*args):
        lis=self.move_to_prev_record_one_book('books',self.index_books_reg)
        
        if len(lis)==0:
            self.show_nav_anim(nav,'pics\\noti.png',\
                                                  '[b]Reached the first record ![/b]',1)
        else:
            recs=lis[0]
        
            controls['acc_n'].text=str(recs[0])
            controls['isbn'].text=str(recs[2])
            controls['tit'].text=str(recs[3])
            controls['pubr'].text=str(recs[4])
            controls['edition'].text=str(recs[5])
            controls['auth'].text=str(recs[6])
            controls['pob'].text=str(recs[7])
            controls['yop'].text=str(recs[8])
            controls['categ'].text=str(recs[9])
            controls['shelve'].text=str(recs[10])
            
            self.index_books_reg-=1
            file=open('index_books_reg.txt','w')
            file.write(str(self.index_books_reg))
            file.close()
        
        
        
    def move_to_first_record_one_book(self,table,*args):
        self.cursor.execute('''SELECT * FROM {} ORDER BY id ASC LIMIT 1'''.format(table.replace('"','""')))
        rec=self.cursor.fetchall()
        return rec
        
        
    def move_to_last_record_one_book(self,table,*args):
        self.cursor.execute('''SELECT * FROM {} ORDER BY id DESC LIMIT 1'''.format(table.replace('"','""')))
        rec=self.cursor.fetchall()
        return rec

    def move_to_next_record_one_book(self,table,index_no,*args):
        self.cursor.execute('''SELECT * FROM {} WHERE id > ? ORDER BY id ASC LIMIT 1'''.format(table.replace('"', '""')),(index_no,))
        rec=self.cursor.fetchall()
        return rec

    def move_to_prev_record_one_book(self,table,index_no,*args):
        self.cursor.execute('''SELECT * FROM {} WHERE id < ? ORDER BY id DESC LIMIT 1'''.format(table.replace('"','""')),(index_no,))
        rec=self.cursor.fetchall()
        return rec

    def change_to_one_reg(self):
        self.screen_book_reg.index=0
    
    def change_to_many_reg(self):
        self.screen_book_reg.index=1

    def show_nav_anim(self,navigator,image,content,anim_duration=2,controls='',*args):
        navigator.sm.current='results'
        navigator.img.source=image
        navigator.img.reload()
        navigator.lbl_i.text=content
        if controls !='':
            controls['add_r'].disabled=True
            controls['del_r'].disabled=True
        
        Clock.schedule_once(partial(self.unshow_nav_anim,navigator,controls),anim_duration)
        
    def unshow_nav_anim(self,navigator,controls,*args):
        navigator.sm.current='main'
        if controls !='':
            controls['add_r'].disabled=False
            controls['del_r'].disabled=False

    ################################################ LOAD DETAILS FROM THE INTERNET
    def fill_form_with_online(self,title, isbn, auth, publ, yp):
        if title=='': title='none'
        if isbn=='': isbn='none'
        if auth =='': auth='none'
        if publ=='': publ='none'
        if yp=='': yp='none'
        
        if self.screen_book_reg.index==0:
            self.one_book_scroll_inputs['tit'].text=title
            self.one_book_scroll_inputs['isbn'].text=isbn[6:]
            self.one_book_scroll_inputs['auth'].text=auth[8:]
            self.one_book_scroll_inputs['pubr'].text=publ[11:]
            self.one_book_scroll_inputs['yop'].text=yp[6:]
            self.one_book_scroll_inputs['edition'].text='none'
            self.one_book_scroll_inputs['pob'].text='none'
            
            
        else:
            self.many_book_scroll_inputs['tit'].text=title
            self.many_book_scroll_inputs['isbn'].text=isbn[6:]
            self.many_book_scroll_inputs['auth'].text=auth[8:]
            self.many_book_scroll_inputs['pubr'].text=publ[11:]
            self.many_book_scroll_inputs['yop'].text=yp[6:]
            self.many_book_scroll_inputs['edition'].text='none'
            self.many_book_scroll_inputs['pob'].text='none'
            
            
        
    def load_internet_controls(self,value, *args):
        threading.Thread(target=self.load_cards_for_net,args=(value,)).start()

    @mainthread
    def enter_isbn(self,enter=False,no_re=False,in_v=False,net=False):
        if enter==True:
            self.show_notification('Enter an isbn or a book title to search',5)
        elif no_re==True:
            self.show_notification('No results found!',5)
        elif in_v==True:
            self.show_notification('Invalid isbn please check your isbn and retry !',5)
        elif net==True:
            self.show_notification('No Internet connection!',5)

    

    @mainthread
    def loading_bar_card(self):
    
        global load_bar
        load_bar=Image(size_hint=(None,None),source='pics\\load.gif',size=(40,40),pos_hint={'center_x':.9,'center_y':.6},mipmap=True)    
        self.cardholder_bk_reg.ids.float1.add_widget(load_bar)
        

    
    def load_cards_for_net(self,value,*args):
        value = self.ids.online_t.ids.txt.text
      
        self.scroll_online.clear_widgets()
        clean_value=value.replace('-','')
        #check whether the value is numeric or alphabetic
        if clean_value=='':
            self.enter_isbn(True)
            
        #search book by isbn
        elif clean_value.isnumeric()==True:
            self.ids.online_s.disabled=True
            self.loading_bar_card()
            #check for an internet connection
            try:
                urllib.request.urlopen('http://google.com')
                #there is connection
                iconnection=True
                
            except urllib.error.URLError:
                #no connection
                iconnection=False
                self.enter_isbn(False,False,False,True)
                self.ids.online_s.disabled=False
                self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
            
            if iconnection==True:
                
                try:
                    #fetch data from the internet
                    info=isbnlib.meta(clean_value,  service='goob')
                    
                    if info==None:
                        self.enter_isbn(False,True)
                        self.ids.online_s.disabled=False
                        self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
                    else:
                        isb='isbn :' +info['ISBN-13']
                        title=info['Title']
                        pub='publisher :'+info['Publisher']
                        year='year :'+info['Year']
                        auth='author: '
                        for au in info['Authors']:
                            auth+=' '+au
                        try:
                            imagelinks=isbnlib.cover(info['ISBN-13'])
                            thumbnail=imagelinks['thumbnail']
                            r = requests.get(thumbnail,stream=True)
                            ext = r.headers['content-type'].split('/')[-1] # converts response headers mime type to an extension (may not work with everything)
                            with open("%s.%s" % (1, ext), 'wb') as f:
                                for chunk in r.iter_content(1024):
                                    f.write(chunk)
                        except:
                            ext='pics\\thumb.jpg'
                                    
                        #create the button and add it to the scroll
                        self.onlineb=Online_b(isbn=isb,titl=title\
                                          ,auth=auth,publ=pub,year=year,\
                                          size_hint=(.8,None),height=200)
                        
                        Clock.schedule_once(partial(self.load_picture,'1',ext),1)
                                
                        self.scroll_online.add_widget(self.onlineb)
                        self.ids.online_s.disabled=False
                        self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
                        
                except isbnlib._exceptions.NotValidISBNError:
                    self.enter_isbn(False,False,True)
                    self.ids.online_s.disabled=False
                    self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
                
        else:
            self.ids.online_s.disabled=True
            self.loading_bar_card()
            #check for an internet connection
            try:
                urllib.request.urlopen('http://google.com')
                #there is connection
                iconnection=True
            except urllib.error.URLError:
                #no connection
                iconnection=False
                self.enter_isbn(False,False,False,True)
                self.ids.online_s.disabled=False
                self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
                
            
            if iconnection==True:
                try:
                    #fetch data from the internet
                    info=goom(value)
                    total_books=len(info)
                    for no in range(total_books):
                        isb='isbn :' +info[no]['ISBN-13']
                        title=info[no]['Title']
                        pub='publisher :'+info[no]['Publisher']
                        year='year :'+info[no]['Year']
                        auth='author: '
                        for au in info[no]['Authors']:
                            auth+=' '+au
                        
                            #creates the image
                            try:
                                imagelinks=isbnlib.cover(info[no]['ISBN-13'])
                                thumbnail=imagelinks['thumbnail']
                            
                                r = requests.get(thumbnail,stream=True)
                                ext = r.headers['content-type'].split('/')[-1] # converts response headers mime type to an extension (may not work with everything)
                                with open("%s.%s" % (no,ext), 'wb') as f:
                                    for chunk in r.iter_content(1024):
                                        f.write(chunk)
                            except:
                                ext='jpg'
                                no='pics\\thumb'


                        #create the button and add it to the scroll
                        self.onlineb=Online_b(isbn=isb,titl=title\
                                          ,auth=auth,publ=pub,year=year,\
                                      size_hint=(.8,None),height=200)
                        try:
                            Clock.schedule_once(partial(self.load_picture,no,ext),1)
                        except:
                            Clock.schedule_once(partial(self.load_picture,no,'jpg'),1)
                            
                        self.scroll_online.add_widget(self.onlineb)

                    self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
                    self.ids.online_s.disabled=False
                    
                except isbnlib._exceptions.NotValidISBNError:
                    self.enter_isbn(False,False,True)
                    self.ids.online_s.disabled=False
                    self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
                except isbnlib.dev._exceptions.NoDataForSelectorError:
                    self.enter_isbn(False,True)
                    self.ids.online_s.disabled=False
                    self.cardholder_bk_reg.ids.float1.remove_widget(load_bar)
                
                         
    @mainthread
    def load_picture(self,no,ext,*args):
        self.onlineb.img.source='%s.%s'%(no,ext)
        
        
class Lists_widget(MDLabel):
    wg = StringProperty()
    def __init__(self, **kwargs):
        super(Lists_widget, self).__init__(**kwargs)
        

class Scroller0(ScrollView):
    def __init__(self, **kwargs):
        super(Scroller0, self).__init__(**kwargs)
        self.bar_width=0
        self.scroll_type=['bars']
        
        
class Recv(RecycleView):
    def __init__(self, **kwargs):
        super(Recv, self).__init__(**kwargs)

        self.bar_width=12
        self.scroll_type=['bars']
        
        
    def on_scroll_start(self, touch, check_children=True):
        self.parent.parent.parent.h_scroll.scroll_x=self.scroll_x
        
        return RecycleView.on_scroll_start(self, touch, check_children=check_children)
    
    def on_scroll_move(self, touch):
        self.parent.parent.parent.h_scroll.scroll_x=self.scroll_x
        
        return RecycleView.on_scroll_move(self, touch)
    
    def on_scroll_stop(self, touch, check_children=True):
        self.parent.parent.parent.h_scroll.scroll_x=self.scroll_x
        
        return RecycleView.on_scroll_stop(self, touch, check_children=check_children)
        
class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleGridLayout):
    
    ''' Adds selection and focus behaviour to the view. '''
    def get_nodes(self):
        nodes = self.get_selectable_nodes()
        if self.nodes_order_reversed:
            nodes = nodes[::-1]
        if not nodes:
            return None, None

        selected = self.selected_nodes
        if not selected:  # nothing selected, select the first
            self.select_node(nodes[0])
            return None, None

        if len(nodes) == 1:  # the only selectable node is selected already
            return None, None

        last = nodes.index(selected[-1])
        self.clear_selection()
        return last, nodes

    def select_nxt(self):
        last, nodes = self.get_nodes()
        if not nodes:
            return

        if last == len(nodes) - 1:
            self.select_node(nodes[0])
        else:
            self.select_node(nodes[last + 1])

    def select_previous(self):
        last, nodes = self.get_nodes()
        if not nodes:
            return

        if not last:
            self.select_node(nodes[-1])
        else:
            self.select_node(nodes[last - 1])
    
                
class SelectableLabel(RecycleDataViewBehavior, Lists_widget):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)
        
    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        pass

class TableWidget(BoxLayout):
    recv_add=ObjectProperty()
    v_scroll=ObjectProperty()
    h_scroll=ObjectProperty()
    grid_me=ObjectProperty()
    db_l0=ObjectProperty()
    
    def __init__(self, **kwargs):
        super(TableWidget, self).__init__(**kwargs)
        
    def clear(self):
        self.recv_add.data = []

    def insert(self, value):
        self.recv_add.data.insert(3, {'text': value })

    def remove(self,index):
        if self.recv_add.data:
            self.recv_add.data.pop(index)

    def update(self,index, value):
        self.recv_add.data[index]['text']= value
        self.recv_add.refresh_from_data()

    
class MainApp(App):
    #theme_cls = ThemeManager()
    
    def build(self):
        self.title='Quora Library Management system'
        self.icon ='pic_control\\icon.ico'
        self.Sm = ScreenM()
        return self.Sm
      
    def on_stop(self):
        pass

if __name__=='__main__':
    MainApp().run()
