app_name = "nexlify_estimation"
app_title = "Nexlify Estimation"
app_publisher = "Kamal Adel"
app_description = "Estimation Engine for ERPNext"
app_email = "Kamal.adel@outlook.com"
app_license = "mit"

# ربط ملف الجافاسكريبت بصفحة التقديرات
doctype_js = {
    "Project Estimation": "public/js/estimation_controller.js"
}


export_python_type_annotations = True
require_type_annotated_api_methods = True

fixtures = [
    {"doctype": "Custom Field"},
    {"doctype": "Property Setter"},
    {"doctype": "Client Script"},
    {"doctype": "Server Script"},

]