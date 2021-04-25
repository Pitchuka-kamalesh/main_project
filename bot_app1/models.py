from django.db import models

# Create your models here.

class Treatment_Model(models.Model):

    province_state = models.CharField(max_length = 20)
    country = models.CharField(max_length= 50)
    uwi = models.IntegerField()
    active_ind = models.CharField(max_length = 10)
    source = models.CharField(max_length= 50)
    license_id = models.CharField(max_length= 50)
    dril_id   = models.IntegerField()
    comp_source = models.CharField(max_length= 50)
    comp_obs_no = models.CharField(max_length= 50)
    changeby = models.CharField(max_length= 50)
    changedate = models.DateField()
    created_by = models.CharField(max_length= 50)
    created_date = models.DateField()
    treatment_obs_no = models.IntegerField()
    stageno = models.IntegerField()
    treatment_top = models.IntegerField()
    treatment_base = models.IntegerField()
    total_no_of_statges = models.IntegerField()
    casing_ind_type = models.CharField(max_length= 50)
    data_source = models.CharField(max_length= 50)
    line_ind = models.IntegerField()
    treatment_type = models.CharField(max_length= 50)
    simulaton_type = models.CharField(max_length= 50)
    pressure_pump_co = models.IntegerField()
    treatment_co = models.CharField(max_length= 50)
    top_strait_unit_id = models.CharField(max_length= 50)
    top_age = models.IntegerField()
    base_strait_unit_id = models.CharField(max_length= 50)
    base_age = models.IntegerField()
    treatment_remark = models.CharField(max_length= 50)

    class Meta:
        db_table = "Treatment"
    
