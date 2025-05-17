# ToDo API with Django REST Framework 

هذا المشروع عبارة عن API لإدارة المهام (ToDo List) باستخدام Django وDjango REST Framework مع دعم التوثيق باستخدام JWT.

## الميزات

- تسجيل المستخدمين وتسجيل الدخول باستخدام JWT.
- CRUD كامل على المهام (إنشاء، قراءة، تعديل، حذف).
- كل مستخدم يرى فقط المهام الخاصة به.
- الخصوصية مفعلة: لا يمكن تعديل أو حذف مهام مستخدم آخر.
- API نظيف وسهل الاستخدام (يدعم Postman أو أي أداة مشابهة).

---

## التقنيات المستخدمة

- Python 3.x
- Django 4.2
- Django REST Framework
- Simple JWT


## التثبيت والتشغيل

1. **استنساخ المشروع:**


###### git clone https://github.com/rahafha1/ToDo_api_project
 cd to your path 


## تفعيل البيئة الافتراضية:
python -m venv venv
.\venv\Scripts\activate  


## تثبيت المتطلبات 
pip install -r requirements.txt

## تشغيل السيرفر 
python manage.py migrate
python manage.py runserver


## tests :

#### Register :
POST /api/register/
JSON EX :
{
  "username": "user1",
  "password": "your_password"
}
response :
 JSON :
 {
 your "user name"
 }
#### login :
POST /api/token/
JSON EX :

{
  "username": "user1",
  "password": "your_password"
}
response : 
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
note  : copy your access token to use it in authorization in order to apply CRUD your ToDo tasks .
#### refresh token 
note : the access token is only valid for 1 hour so you may need to refresh it :) 

POST /api/token/refresh/
JSON EX :
{
  "refresh": "your_refresh_token"
}

#### ToDo Endpoints (CRUD)
 ###### note: pass the token in the header 
 ###### Authorization: Bearer your_access_token


 ##### create new todo :
 POST /api/todos/
 json:
 {
  "title": "مهمة جديدة",
  "description": "تفاصيل المهمة",
  "completed": false
}

#####  view todo by id 

GET /api/todos/1/
responce :
[
  {
    "id": 1,
    "title": "مهمة 1",
    "description": "تفاصيل المهمة",
    "completed": false
  }
]

#####  edit todo 
PUT /api/todos/<id>/
json:
{
  "title": "عنوان جديد",
  "description": "تفاصيل جديدة",
  "completed": true
}

#####  delete todo 
DELETE /api/todos/<id>/


## privacy tests : 
##### كل مستخدم يمكنه فقط رؤية مهامه:
##### استخدم توكن مستخدم A → سترى فقط مهامه.
##### استخدم توكن مستخدم B → سترى فقط مهامه.
##### عند استخدام توكن لمستخدم ليس مالكًا لمهام، يظهر الرد:[EMPTY]

