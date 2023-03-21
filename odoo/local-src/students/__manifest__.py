{
    "name": "Gestion des étudiants",
    "version": "0.4",
    "category": "Generic Modules/Others",
    "description": """Test création module gestion des étudiants dans Odoo v14""",
    "author": "Vernier",
    "data": [
        "security/students_security.xml",
        "views/students_views.xml",
        "security/ir.model.access.csv",
            "views/assets.xml",
             "views/training_views.xml",
             "views/mark_views.xml",
             "views/studentscontinuous_views.xml",
             "views/res_partner_views.xml",
             "reports/students_report.xml",

       #      "data/students_training_data.xml",
        #     "data/students_student_data.xml",
         #    "data/students_mark_data.xml",
            ],

    "depends": ["base", "web"], #mettre ici quand on utilise un module
    "installable": True,
    "Auto_install": False,
}
