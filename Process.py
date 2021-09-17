import pandas as pd

import Connection as conn


###################################################################################################
# Como deve ser o banco do google:                                                                #
#                                                                                                 #
# First Name | Last Name | Email Address| Password| Org Unit Path|Change Password at Next Sign-In|#
# Title      | "Síntese" | email Síntese| CPF     | "/Trainee"   | True                           #
#                                                                                                 #
###################################################################################################

###################################################################################################
# Como deve ser o banco do Pypefy:                                                                #
#                                                                                                 #
# Title                 | Email síntese       | CPF              |                                #
# "Nome do membro"      | email@Sintese.com.br| XXX.XXX.XXX - XX |                                #
#                                                                                                 #
###################################################################################################
class Process:

    def __init__(self, path):
        connection = conn.Connection(path)
        self.original = connection.db

        database = pd.DataFrame()
        database['First Name'] = self.original['Title']
        database['Last Name'] = "- Sintese"  # Sobrenome é obrigatorio no google, então coloquei Sintese para padronizar
        database['Email address'] = self.original['Email Síntese']
        database['Password'] = self.original['CPF']
        database['Org Unit Path'] = "/Trainee"
        database['Change Password at Next Sign-In'] = True
        self.membrosEmail = pd.DataFrame()
        self.membrosEmail['Member Email'] = database['Email address']
        self.membrosEmail['Group Email'] = "membros@sintesejr.com.br"
        self.final = database