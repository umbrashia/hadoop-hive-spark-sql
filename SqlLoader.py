class SqlLoader:
    selectList = list()
    tableName = ""
    whereList = list()

    def table(self, tableName):
        self.tableName = tableName
        return self

    def join(self,tableName,whereText,joinType="join"):
        if joinType=='join':
            print("ohh join")

    async def doThread(self, parameter_list):
        print("Jai Ho")

    def select(self, value):
        self.selectList.append(value)
        return self

    def where(self,key,value,operator="="):
        self.whereList.append(key+" "+operator+" '"+value+"'")

    def get(self):
        return "select "+("".join(self.selectList))+" from "+self.tableName
