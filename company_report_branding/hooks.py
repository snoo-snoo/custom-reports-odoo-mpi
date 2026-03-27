# -*- coding: utf-8 -*-

import secrets


def post_init_hook(env):
    companies = env['res.company'].search(['|', ('crb_asset_token', '=', False), ('crb_asset_token', '=', '')])
    for company in companies:
        company.write({'crb_asset_token': secrets.token_urlsafe(24)})
