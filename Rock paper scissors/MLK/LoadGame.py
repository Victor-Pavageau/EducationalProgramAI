from mlforkids import MLforKidsImageProject

key = "3c04f950-6e0a-11ec-9f92-5b6cfb4e84b1d0858e99-7cc2-47fa-812e-519ccc7a3af1"

def LoadProject():
    myproject = MLforKidsImageProject(key)
    myproject.train_model()
    return myproject