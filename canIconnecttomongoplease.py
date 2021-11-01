from pymodm import MongoModel, connect, fields

connect("mongodb+srv://amey:fanyuan@cluster0.dovib.mongodb.net/"+
            "HealthDatabase?retryWrites=true&w=majority")


class User(MongoModel):
    name = fields.CharField()


x = User("Dave Saves")
x.save()