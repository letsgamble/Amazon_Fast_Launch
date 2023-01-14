import pandas as pd
import PySimpleGUI as sg


def gui_app():
    fl = FastLaunch(tcorp_file='tcorp.csv', weekly_file='weekly.xlsx')

    sg.theme('SystemDefault')
    layout = [[sg.Text(
        'This program automatically extract Parent Classes to be launched.')],
        [sg.Text(
            'In the program directory please provide two files (case sensitive):')],
        [sg.Text(
            'weekly.xlsx - Classes list, provided on a weekly basis')],
        [sg.Text(
            'tcorp.csv - Finished tickets exported from the t.corp')],
        [sg.Text(
            'Output will be saved to a file named To_Launch.csv')],
        [sg.Text(
            '')],
        [sg.Button('START'), sg.Button('EXIT')],
        [sg.Text(
            '')],
        [sg.Text(
            'Reach me out: kawesolo@amazon.pl')],
    ]
    window = sg.Window('Amazon_Fast_Launch ver. 1.0', layout,
                       element_justification='c')

    while True:
        event, values = window.read()
        if event == 'START':
            fl.import_files()
            fl.iter_tcorp_rows()
            fl.look_in_dataframes()
            fl.save_to_csv()
        if event == sg.WIN_CLOSED or event == 'EXIT':
            break
    window.close()


class FastLaunch:
    def __init__(self, weekly_file, tcorp_file):
        self.weekly_file = weekly_file
        self.tcorp_file = tcorp_file
        self.newrule_list = []
        self.other_rules_list = []
        self.df_list = []
        self.sheets_list = []

    def import_files(self):
        xl = pd.ExcelFile(self.weekly_file)

        for val in xl.sheet_names:
            if 'Pivot' not in val:
                self.sheets_list.append(val)
        self.df_tcorp = pd.read_csv(self.tcorp_file)
        self.df_tcorp.sort_values(["Severity"], axis=0, ascending=True, inplace=True)

        self.df_1 = pd.read_excel(self.weekly_file, sheet_name=self.sheets_list[0])
        self.df_list.append(self.df_1)

        try:
            self.df_2 = pd.read_excel(self.weekly_file, sheet_name=self.sheets_list[1])
            self.df_list.append(self.df_2)
        except IndexError:
            ...

        try:
            self.df_3 = pd.read_excel(self.weekly_file, sheet_name=self.sheets_list[2])
            self.df_list.append(self.df_3)
        except IndexError:
            ...

        try:
            self.df_4 = pd.read_excel(self.weekly_file, sheet_name=self.sheets_list[3])
            self.df_list.append(self.df_4)
        except IndexError:
            ...

        try:
            self.df_5 = pd.read_excel(self.weekly_file, sheet_name=self.sheets_list[4])
            self.df_list.append(self.df_5)
        except IndexError:
            ...

        try:
            self.df_6 = pd.read_excel(self.weekly_file, sheet_name=self.sheets_list[5])
            self.df_list.append(self.df_6)
        except IndexError:
            ...

    def iter_tcorp_rows(self):
        for idx, row in self.df_tcorp.iterrows():
            if str('NR') in str(row["Title"]):
                if str(':/') in str(row["Title"]):
                    rule_name = str(row["Title"]).split(":/")
                    self.newrule_list.append(str('/') + rule_name[1])
                else:
                    self.newrule_list.append(row["Title"])
            else:
                if str(':/') in str(row["Title"]):
                    rule_name = str(row["Title"]).split(":/")
                    self.other_rules_list.append(str('/') + rule_name[1])
                else:
                    self.other_rules_list.append(row["Title"])

    def look_in_dataframes(self):
        all_to_launch = []
        for val in self.newrule_list:
            for df in self.df_list:
                to_launch = df.loc[df['child_class'] == val, 'parent_class']
                all_to_launch.append(val)
                if len(to_launch) > 0:
                    val_to_extend = to_launch.tolist()
                    all_to_launch.extend(val_to_extend)
        for val in self.other_rules_list:
            for df in self.df_list:
                to_launch = df.loc[df['child_class'] == val, 'parent_class']
                if len(to_launch) > 0:
                    val_to_extend = to_launch.tolist()
                    all_to_launch.extend(val_to_extend)
        self.output = list(set(all_to_launch))

    def save_to_csv(self):
        df = pd.DataFrame(self.output)
        df.to_csv('To_Launch.csv', index=False, header=False)


gui_app()
