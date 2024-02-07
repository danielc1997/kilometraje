# -*- coding: utf-8 -*-
from odoo import models, fields, api


class agenda(models.Model):
     _name = 'agenda.agenda'
     _description = 'agenda.agenda'

     tecnico = fields.Selection([('Andres Cajas','Andres Cajas'),('Xavier Tituaña','Xavier Tituaña')])
     kilometraje_inicial = fields.Integer(required=True, string="Kilometraje inicial")
     kilometraje_final = fields.Integer(required=True,string="Kilometraje final")
     fecha_kilometraje = fields.Datetime(required=True,string="Fecha del kilometraje")
     valor_combustible_personal= fields.Char(required=True ,string="Valor kilometraje personal")
     valor_combustible_laboral= fields.Char(required=True,string="Valor kilometraje laboral")
     observacion= fields.Char()
     imagen_inicial = fields.Binary(required=True ,string="Fotografia kilometraje inicial")
     imagen_final = fields.Binary(required=True,string="Fotografia kilometraje final")
     kilometraje_total= fields.Integer(required=True,string="Kilometraje total del dia")
     area = fields.Selection([('Soporte técnico','Soporte técnico'),('Instalaciones','Instalaciones'),('Infraestructura','Infraestructura')],string="Area encargada")
     @api.onchange('kilometraje_inicial', 'kilometraje_final')
     def onchange_field(self):
        if self.kilometraje_inicial or self.kilometraje_final:
            self.kilometraje_total = self.kilometraje_final - self.kilometraje_inicial