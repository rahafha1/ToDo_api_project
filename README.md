# ToDo API with Django REST Framework 📝

هذا المشروع عبارة عن API لإدارة المهام (ToDo List) باستخدام Django وDjango REST Framework مع دعم التوثيق باستخدام JWT.

## ✅ الميزات

- تسجيل المستخدمين وتسجيل الدخول باستخدام JWT.
- CRUD كامل على المهام (إنشاء، قراءة، تعديل، حذف).
- كل مستخدم يرى فقط المهام الخاصة به.
- الخصوصية مفعلة: لا يمكن تعديل أو حذف مهام مستخدم آخر.
- API نظيف وسهل الاستخدام (يدعم Postman أو أي أداة مشابهة).

---

## 🧱 التقنيات المستخدمة

- Python 3.x
- Django 4.2
- Django REST Framework
- Simple JWT


## ⚙️ التثبيت والتشغيل

1. **استنساخ المشروع:**


git clone https://github.com/rahafha1/ToDo_api_project
cd ToDo_api_project


## تفعيل البيئة الافتراضية:
python -m venv venv
venv\Scripts\activate   # على ويندوز


## تثبيت المتطلبات 
pip install -r requirements.txt

## تشغيل السيرفر 
python manage.py migrate
python manage.py runserver


## tests :
POST /api/register/

{
  "username": "user1",
  "password": "your_password"
}
 2-login :
POST /api/token/

{
  "username": "user1",
  "password": "your_password"
}
responce : 
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
3- refresh token 
POST /api/token/refresh/
{
  "refresh": "your_refresh_token"
}
4-ToDo Endpoints (CRUD)
 note: pass the token in the header 
 Authorization: Bearer your_access_token


 4-1 create new todo :
 POST /api/todos/
 json:
 {
  "title": "مهمة جديدة",
  "description": "تفاصيل المهمة",
  "completed": false
}

4-2 view todo by id 

GET /api/todos/1
responce :
[
  {
    "id": 1,
    "title": "مهمة 1",
    "description": "تفاصيل المهمة",
    "completed": false
  }
]

4-3 edit todo 
PUT /api/todos/<id>/
json:
{
  "title": "عنوان جديد",
  "description": "تفاصيل جديدة",
  "completed": true
}

4-4 delete todo 
DELETE /api/todos/<id>/


## privacy tests : 
✔️ كل مستخدم يمكنه فقط رؤية مهامه:
استخدم توكن مستخدم A → سترى فقط مهامه.

استخدم توكن مستخدم B → سترى فقط مهامه.

✅ تمت تجربة ذلك ونجح:
عند استخدام توكن لمستخدم ليس مالكًا لمهام، يظهر الرد:
[ empty]

