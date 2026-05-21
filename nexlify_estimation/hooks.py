app_name = "nexlify_estimation"
app_title = "Nexlify Estimation"
app_publisher = "Kamal Adel"
app_description = "Estimation Engine for ERPNext"
app_email = "Kamal.adel@outlook.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "nexlify_estimation",
# 		"logo": "/assets/nexlify_estimation/logo.png",
# 		"title": "Nexlify Estimation",
# 		"route": "/nexlify_estimation",
# 		"has_permission": "nexlify_estimation.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nexlify_estimation/css/nexlify_estimation.css"
# app_include_js = "/assets/nexlify_estimation/js/nexlify_estimation.js"

# include js, css files in header of web template
# web_include_css = "/assets/nexlify_estimation/css/nexlify_estimation.css"
# web_include_js = "/assets/nexlify_estimation/js/nexlify_estimation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nexlify_estimation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "nexlify_estimation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "nexlify_estimation.utils.jinja_methods",
# 	"filters": "nexlify_estimation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "nexlify_estimation.install.before_install"
# after_install = "nexlify_estimation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nexlify_estimation.uninstall.before_uninstall"
# after_uninstall = "nexlify_estimation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "nexlify_estimation.utils.before_app_install"
# after_app_install = "nexlify_estimation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "nexlify_estimation.utils.before_app_uninstall"
# after_app_uninstall = "nexlify_estimation.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "nexlify_estimation.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nexlify_estimation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nexlify_estimation.tasks.all"
# 	],
# 	"daily": [
# 		"nexlify_estimation.tasks.daily"
# 	],
# 	"hourly": [
# 		"nexlify_estimation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nexlify_estimation.tasks.weekly"
# 	],
# 	"monthly": [
# 		"nexlify_estimation.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "nexlify_estimation.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "nexlify_estimation.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nexlify_estimation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nexlify_estimation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nexlify_estimation.utils.before_request"]
# after_request = ["nexlify_estimation.utils.after_request"]

# Job Events
# ----------
# before_job = ["nexlify_estimation.utils.before_job"]
# after_job = ["nexlify_estimation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"nexlify_estimation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

