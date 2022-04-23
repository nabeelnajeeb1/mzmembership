frappe.ready(function() {
	/*
	frappe.web_form.on('email', (field, value) => {
		let data = frappe.web_form.get_value("email");

		if(data){
			frappe.call({
				"method": "mesalumniapp.mes_alumni.web_form.mes_alumni_association_member_registration.mes_alumni_association_member_registration.check_user",
				"args": {"email": data},
				"callback": function(r){
					var data = r.message;
					if(r.message == true){
						frappe.throw(_("Already Registered Email"));
						frappe.web_form.set_value("email", '');
					}
				}
			});
		}
	});*/
})
