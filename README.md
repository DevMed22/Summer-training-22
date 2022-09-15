# Summer-training-22
## Idea and Functionality
Our project is about a health center through which patients can register an appiontment with the different sections in the health center. 
<br>
Doctors can share there tips and news through posts on the website.
<br><br>
Through our system, we make health care better as patients can see available times in the section and book it. Also doctors can know details about their patients before the come to health center and all data will be stored to come back to it when needed.
<br><br>
We have used deep learning model to help patient diagnose his case with intial result before visiting the Doctor. You can find it named [Covid-19](https://github.com/DevMed22/Summer-training-22/tree/main/AI/Covid-19_Detection)

## Backend and Frontend
We used Django as the main backend framework and for the  frontend we used bootstrap. 
<br><br>
## Machine Learning
We have built several deep learning models to help us in our system and you can check them in [AI directory](https://github.com/DevMed22/Summer-training-22/tree/main/AI) .
We have 4 models:
- Covid-19_Detection model is the one we deployed inside our main project. You can use it to upload image and check if the the case has Covid-19 or not.
- CellOrganelles-ObjectSegmentation model is the one we deployed inside HIS-Pathology task. You can upload an image and make a segmentation of the organelles inside the blood.
- Blood-cells-detection model is a flask app that can be run separatly.
- cells-object-detection model 
<br>
We have used Flask, Streamlit to deploy our models and Tensorflow, SKlearn, Numpy, Pandas and Matplotlib for buidling our models.
<br><br>

## Hosting
We deployed our project and hosted it on Microsoft Azure and you can check the live version on [Microsoft Azure](https://health-center-22.azurewebsites.net/)
<br><br>

## GitHub Actions and Automation
We are using GitHub Actions to automate testing whenever new push or pull request are made to the main branch.
you can find the workflow automation file inside this [directory](https://github.com/DevMed22/Summer-training-22/tree/main/.github/workflows) .
<br>
You can check workflow history and see the magic [here](https://github.com/DevMed22/Summer-training-22/actions)
<br><br>

## Steps to run Django Project
- clone repo and create virtual environment
- install project requirements throgh file Requirements.txt  (pip install -r requirements.txt)
- make migration using cli (python manage.py migrate)
- run django server locally (python manage.py runserver)

Note: to run machine learning model(Covid-19), you need to run it on different port first and then access it from django project

### Team work load
- Ahmed Tarek ->  [Machine Learning models](https://github.com/DevMed22/Summer-training-22/tree/main/AI), Flask (Deployment of Covid-19 and Blood-Cells), Streamlit (Deployment of cell-organnel-object-segmentation)
- Amr Atef -> Django (backend of Health-Center-22), integrating Machine learning models inside Health-Center-22
- Omar Elsherif -> Django (Backend of Health-Center-22), [GitHub Actions](https://github.com/DevMed22/Summer-training-22/tree/main/.github/workflows) (automation of django testing and Continuous Integration with Azure), Hosting on Azure 
- Mohamed Tabana -> Django (Backend of task [HIS-Pathology](https://github.com/DevMed22/Summer-training-22/tree/main/HIS-Pathology))
- Esmael Mosad -> Frontend of Health-Center-22 using HTML, CSS, JavaScript, Bootstrap
- Yasmine Yasser -> Frontend of task [HIS-Pathology](https://github.com/DevMed22/Summer-training-22/tree/main/HIS-Pathology)

#### We learned alot during this project and we are so proud of the result✌️
