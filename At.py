
class Artisan:
    def __init__(self, ID, profile_pic, phone_num, speciality):
        self.ID = ID
        self.profile_pic = profile_pic
        self.phone_num = phone_num
        self.speciality = speciality

    def apply(self):
        print(f"Artisan {self.ID} has applied for a job.")

    def upload(self):
        print(f"Artisan {self.ID} has uploaded new content.")

    def search(self):
        print(f"Artisan {self.ID} is searching for new opportunities.")

    def show_profile_pic(self):
        print(f"Profile picture for Artisan {self.ID}: {self.profile_pic}")



class Client:
    def __init__(self, ID, phone_no):
        self.ID = ID
        self.phone_no = phone_no

    def employ(self, artisan):
        print(f"Client {self.ID} has employed Artisan {artisan.ID}.")

    def search(self):
        print(f"Client {self.ID} is searching for artisans or services.")

    def report(self):
        print(f"Client {self.ID} has reported an issue.")



Khaleed = Artisan(ID=1090, profile_pic="images.jpeg", phone_num="+2349075054687", speciality="Carpentry")
Fuad = Client(ID=1738, phone_no="+2349034098202")


Khaleed.apply()
Fuad.employ(Khaleed)
Khaleed.upload()
Fuad.search()
Fuad.report()
Khaleed.show_profile_pic()
