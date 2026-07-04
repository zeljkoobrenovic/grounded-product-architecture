import json
import os

from product_bricks_support import build_bricks_lookup


def load_json_if_exists(path, default_value):
    if os.path.exists(path):
        return json.load(open(path))
    return default_value


def load_first_existing(paths, default_value):
    for path in paths:
        if os.path.exists(path):
            return json.load(open(path))
    return default_value


def normalize_icon_name(icon_name, fallback='customer.png'):
    value = (icon_name or fallback).strip()
    if not value:
        value = fallback
    while value.endswith('.png.png'):
        value = value[:-4]
    while value.endswith('.svg.png'):
        value = value[:-4]
    if '.' in value:
        return value
    return value + '.png'


def collect_kpis(node, target):
    if not node:
        return
    if node.get('name'):
        target[node['name'].lower()] = {
            'name': node.get('name', ''),
            'description': node.get('description', ''),
            'unit': node.get('unit', ''),
            'currentValue': node.get('currentValue', ''),
            'link': node.get('link', ''),
            'linkLabel': node.get('linkLabel', '')
        }
    for child in node.get('children', []):
        collect_kpis(child, target)


def build_customers_lookup(customers):
    customer_icon_map = {
        'house-search': 'seeker.png',
        'owner-key': 'owner.png',
        'briefcase-building': 'intermediary.png'
    }

    lookup = {}
    kpi_lookup = {}

    for group in customers:
        group_name = group.get('group', '')
        for customer in group.get('customers', []):
            lookup[customer['id']] = {
                'id': customer['id'],
                'name': customer.get('name', customer['id']),
                'group': group_name,
                'icon': normalize_icon_name(customer_icon_map.get(customer.get('icon', ''), customer.get('icon', 'customer.png')))
            }

            pyramids = customer.get('kpiPyramids', {})
            customer_map = {}
            business_map = {}
            collect_kpis(pyramids.get('customerOutcomes', {}).get('top'), customer_map)
            collect_kpis(pyramids.get('businessOutcomes', {}).get('top'), business_map)
            for branch in pyramids.get('customerOutcomes', {}).get('branches', []):
                collect_kpis(branch, customer_map)
            for branch in pyramids.get('businessOutcomes', {}).get('branches', []):
                collect_kpis(branch, business_map)
            kpi_lookup[customer['id']] = {
                'customer': customer_map,
                'business': business_map
            }

    return lookup, kpi_lookup
