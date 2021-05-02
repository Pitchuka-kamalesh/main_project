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
    
class PerformanceModel(models.Model):

    uwi = models.IntegerField()
    source = models.CharField(max_length = 50)
    perforation_obs_no = models.IntegerField()
    completion_obs_no = models.IntegerField()
    active_ind = models.CharField(max_length = 50)
    top_depth = models.IntegerField()
    top_depth_uom = models.CharField(max_length = 50)
    top_tvd_depth = models.CharField(max_length = 50,null=True, blank=True)
    top_tvd_depth_uom = models.CharField(max_length = 50,null= True,blank=True)
    base_depth = models.IntegerField()
    base_depth_uom = models.CharField(max_length = 50)
    base_reservoir = models.CharField(max_length = 50,null=True, blank=True)
    base_tvd_depth = models.IntegerField(null = True, blank =True)
    base_tvd_depth_uom = models.CharField(max_length = 50,null=True, blank=True)
    top_strat_unit_id = models.CharField(max_length = 50)
    top_strat_age = models.IntegerField()
    base_strat_unit_id = models.CharField(max_length = 50)
    base_strat_age = models.IntegerField()
    perforation_date = models.DateTimeField()
    completion_source = models.CharField(max_length = 50,null =True,blank=True)
    completion_status = models.CharField(max_length = 50,null = True,blank=True)
    perforation_angle = models.FloatField(null =True,blank=True)
    completion_status_type = models.CharField(max_length = 50,null =True,blank=True)
    current_status_date = models.DateTimeField(null =True,blank=True)
    perforation_ba_id = models.CharField(max_length = 50,null =True,blank=True)
    perforation_count = models.IntegerField()
    perforation_interval_type = models.CharField(max_length = 50)
    perforation_density = models.CharField(max_length = 50,null =True,blank=True)
    perforation_diameter = models.FloatField()
    perforation_diameter_uom = models.CharField(max_length = 50)
    perforation_method = models.CharField(max_length = 50)
    perforation_per_uom = models.CharField(max_length = 50,null =True,blank=True)
    perforation_phase = models.CharField(max_length = 50,null =True,blank=True)
    perforation_type = models.CharField(max_length = 50,null =True,blank=True)
    cluster_per_stage = models.CharField(max_length = 50,null =True,blank=True)
    row_quality = models.CharField(max_length = 50,null =True,blank=True)
    province_state = models.CharField(max_length = 50)
    remark = models.CharField(max_length = 50,null =True,blank=True)
    charge_type = models.CharField(max_length = 50,null = True,blank = True)
    charge_size = models.IntegerField(null =True,blank=True)
    charge_size_uom = models.CharField(max_length = 50,null =True,blank=True)
    stage_no = models.IntegerField()
    row_changed_by = models.CharField(max_length = 50)
    row_changed_date = models.DateTimeField()
    row_created_by = models.CharField(max_length = 50)
    row_created_date = models.DateTimeField()

    class Meta:
        db_table = "performance"