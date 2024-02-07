# -*- coding: utf-8 -*-
from odoo import models, fields, api


class agenda(models.Model):
     _name = 'agenda.agenda'
     _description = 'agenda.agenda'

     tecnico = fields.Selection([('Andres Cajas','Andres Cajas'),('Xavier Tituaña','Xavier Tituaña')])
     kilometraje_inicial = fields.Integer(required=True)
     kilometraje_final = fields.Integer(required=True)
     fecha_kilometraje = fields.Char(required=True)
     valor_combustible_personal= fields.Char(required=True)
     valor_combustible_laboral= fields.Char(required=True)
     observacion= fields.Char()
     imagen_inicial = fields.Binary(required=True)
     imagen_final = fields.Binary(required=True)
     kilometraje_total= fields.Integer(required=True)
     area = fields.Selection([('Soporte técnico','Soporte técnico'),('Instalaciones','Instalaciones'),('Infraestructura','Infraestructura')])
     @api.onchange('kilometraje_inicial', 'kilometraje_final')
     def onchange_field(self):
        if self.kilometraje_inicial or self.kilometraje_final:
            self.kilometraje_total = self.kilometraje_final - self.kilometraje_inicial