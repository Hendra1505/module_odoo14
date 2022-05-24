from odoo import api, fields, models


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Kursus'
     
    name = fields.Char(string='Judul', required=True)
    description = fields.Text(string='Keterangan')
    user_id = fields.Many2one('res.users', string="Penanggung Jawab")
    session_line = fields.One2many('training.session', 'course_id', string='Sesi')
    product_ids = fields.Many2many('product.product', 'course_product_rel', 'course_id', 'product_id', 'Cendera Mata')
    

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Sesi'
     
    course_id = fields.Many2one('training.course', string='Judul Kursus', required=True, ondelete='cascade')
    name = fields.Char(string='Nama', required=True)
    start_date = fields.Date(string='Tanggal')
    duration = fields.Float(string='Durasi', help='Jumlah Hari Training')
    seats = fields.Integer(string='Kursi', help='Jumlah Kuota Kursi')
    partner_id = fields.Many2one('res.partner', string='Instruktur')


class TrainingAttendee(models.Model):
    _name = 'training.attendee'
    _description = 'Training Peserta'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', 'Partner', required=True, ondelete='cascade')
    name = fields.Char(string='Nama', required=True, inherited=True)
    sex = fields.Selection([('male', 'Pria'), ('female', 'Wanita')], string='Kelamin', required=True, help='Jenis Kelamin')
    marital = fields.Selection([
        ('single', 'Belum Menikah'), 
        ('married', 'Menikah'), 
        ('divorced', 'Cerai')], 
        string='Pernikahan', help='Status Pernikahan')
