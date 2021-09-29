#%%
import numpy as np
import pandas as pd
#%%
class User:
    def __init__(self) -> None:
        self.id = np.random.randint(10000)
        self.articles_read = []



#%%
class ArticleDB:
    def __init__(self):
        self.test = 'a'
        self.load_db()
        self.make_users()
    
    def make_users(self,num=10):
        """"make a list of 10 users"""
        self.users = []
        for i in range(num):
            self.users.append(User())

    def load_db(self):
        """this should connect to airtable but for the moment it is just gen a random file"""
        self.df = pd.DataFrame(np.random.randint(0,2,size=(10, 10)),
                                index = np.random.randint(0,100000,size=(10)))
                    
        self.df["num_read"] = np.random.randint(0,1,size=(10))



    def article_read(self, art_id,user):
        """Mark the article as read by the user, increase the popularity of the article"""
        user.articles_read.append(art_id)
        self.df.loc[art_id].num_read += 1

        


    def suggest_article(self,user):
        """suggest an article to a user"""
        pass

    def suggest_article_new_user(self,user):
        """print out most popular articles"""
        pass



db = ArticleDB()
df = db.df
