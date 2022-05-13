subscript_dict = {
    'layers': ['layer1', 'layer2', 'layer3', 'layer4'],
    'bottom': ['layer4'],
    'lower': ['layer2', 'layer3', 'layer4'],
    'upper': ['layer1', 'layer2', 'layer3'],
    'final sources': ['electricity', 'heat', 'liquids', 'gases', 'solids'],
    'final sources1': ['electricity', 'heat', 'liquids', 'gases', 'solids'],
    'hfc type': ['hfc134a', 'hfc23', 'hfc32', 'hfc125', 'hfc143a', 'hfc152a', 'hfc227ea', 'hfc245ca','hfc4310mee'],
    'households vehicles':
    ['liq 4wheels', 'hib 4wheels', 'elec 4wheels', 'gas 4wheels', 'liq 2wheels', 'elec 2wheels'],
    'materials': [
        'adhesive', 'aluminium', 'aluminium mirrors', 'cadmium', 'carbon fiber', 'cement',
        'chromium', 'copper', 'diesel', 'dy', 'electric div electronic components',
        'evacuation lines', 'fiberglass', 'foam glass', 'galium', 'glass',
        'glass reinforcing plastic', 'gravel', 'indium', 'iron', 'kno3 mined', 'asphalt', 'lime',
        'limestone', 'lithium', 'lubricant', 'magnesium', 'manganese', 'heavy equipment',
        'concrete', 'molybdenum', 'nano3 mined', 'nano3 synthetic', 'neodymium', 'nickel',
        'over grid 15 percentx', 'over grid 5 percentx', 'paint', 'lead', 'plastics',
        'polypropylene', 'rock', 'rock wool', 'sand', 'silicon sand', 'silicon wafer modules',
        'silver', 'site preparation', 'tin', 'soda ash', 'steel', 'synthetic oil', 'tellurium',
        'titanium', 'titanium dioxide', 'vanadium', 'wires', 'zinc'
    ],
    'primary sources': ['coal', 'oil', 'natural gas', 'others'],
    'primary sources1': ['coal', 'oil', 'natural gas', 'others'],

    'rcp scenario': ['rcp26', 'rcp45', 'rcp60', 'rcp85'],
    'res elec': [
        'hydro', 'geot elec', 'solid bioe elec', 'oceanic', 'wind onshore', 'wind offshore',
        'solar pv', 'csp'
    ],
    'res heat': ['solar heat', 'geot heat', 'solid bioe heat'],
    'sectors': [
        'agriculture hunting forestry and fishing', 'mining and quarrying',
        'food beverages and tobacco', 'textiles and textile products',
        'leather leather and footwear', 'wood and products of wood and cork',
        'pulp paper printing and publishing', 'coke refined petroleum and nuclear fuel',
        'chemicals and chemical products', 'rubber and plastics', 'other non metalic mineral',
        'basic metals and fabricated metal', 'machinery nec', 'electrical and optical equipment',
        'transport equipment', 'manufacturing nec recycling', 'electricity gas and water supply',
        'construction',
        'sale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel',
        'wholesale trade and commissions trade except of motor vehicles and motorcycles',
        'retail trade except of motor vehicles and motorcycles repair of household goods',
        'hotels and restaurants', 'inland transport', 'water transport', 'air transport',
        'other supporting and auxiliary transport activities activities of travel agencies',
        'post and telecommunications', 'financial intermediation', 'real estate activities',
        'renting od meq and other business activities',
        'public admin and defence compulsory social security', 'education',
        'health and social work', 'other community social and persona services',
        'private households with employed persons'
    ],
    'sectors1': [
        'agriculture hunting forestry and fishing', 'mining and quarrying',
        'food beverages and tobacco', 'textiles and textile products',
        'leather leather and footwear', 'wood and products of wood and cork',
        'pulp paper printing and publishing', 'coke refined petroleum and nuclear fuel',
        'chemicals and chemical products', 'rubber and plastics', 'other non metalic mineral',
        'basic metals and fabricated metal', 'machinery nec', 'electrical and optical equipment',
        'transport equipment', 'manufacturing nec recycling', 'electricity gas and water supply',
        'construction',
        'sale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel',
        'wholesale trade and commissions trade except of motor vehicles and motorcycles',
        'retail trade except of motor vehicles and motorcycles repair of household goods',
        'hotels and restaurants', 'inland transport', 'water transport', 'air transport',
        'other supporting and auxiliary transport activities activities of travel agencies',
        'post and telecommunications', 'financial intermediation', 'real estate activities',
        'renting od meq and other business activities',
        'public admin and defence compulsory social security', 'education',
        'health and social work', 'other community social and persona services',
        'private households with employed persons'
    ],
    'vehiclet': [
        'hv liq', 'hv hib', 'hv gas', 'lv liq', 'lv elec', 'lv hib', 'lv gas', 'bus liq',
        'bus elec', 'bus hib', 'bus gas', 'train liq', 'train elec'
    ],
    'water color': ['blue water', 'green water', 'gray water'],
    'water0': ['cleanwith pumped water', 'distilledwith deionized water']
}

namespace = {
    'TIME':
    'time',
    'Time':
    'time',
    'historic energy industry own use':
    'historic_energy_industry_own_use',
    'historic final energy intensity by sector and fuel subelectricity subagriculture hunting forestry and fishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subagriculture_hunting_forestry_and_fishing',
    'historic final energy intensity by sector and fuel subelectricity submining and quarrying':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_submining_and_quarrying',
    'historic final energy intensity by sector and fuel subelectricity subfood beverages and tobacco':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subfood_beverages_and_tobacco',
    'historic final energy intensity by sector and fuel subelectricity subtextiles and textile products':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subtextiles_and_textile_products',
    'historic final energy intensity by sector and fuel subelectricity subleather leather and footwear':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subleather_leather_and_footwear',
    'historic final energy intensity by sector and fuel subelectricity subwood and products of wood and cork':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subwood_and_products_of_wood_and_cork',
    'historic final energy intensity by sector and fuel subelectricity subpulp paper printing and publishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subpulp_paper_printing_and_publishing',
    'historic final energy intensity by sector and fuel subelectricity subcoke refined petroleum and nuclear fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic final energy intensity by sector and fuel subelectricity subchemicals and chemical products':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subchemicals_and_chemical_products',
    'historic final energy intensity by sector and fuel subelectricity subrubber and plastics':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subrubber_and_plastics',
    'historic final energy intensity by sector and fuel subelectricity subother non metalic mineral':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subother_non_metalic_mineral',
    'historic final energy intensity by sector and fuel subelectricity subbasic metals and fabricated metal':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subbasic_metals_and_fabricated_metal',
    'historic final energy intensity by sector and fuel subelectricity submachinery nec':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_submachinery_nec',
    'historic final energy intensity by sector and fuel subelectricity subelectrical and optical equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subelectrical_and_optical_equipment',
    'historic final energy intensity by sector and fuel subelectricity subtransport equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subtransport_equipment',
    'historic final energy intensity by sector and fuel subelectricity submanufacturing nec recycling':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_submanufacturing_nec_recycling',
    'historic final energy intensity by sector and fuel subelectricity subelectricity gas and water supply':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subelectricity_gas_and_water_supply',
    'historic final energy intensity by sector and fuel subelectricity subconstruction':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subconstruction',
    'historic final energy intensity by sector and fuel subelectricity subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic final energy intensity by sector and fuel subelectricity subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic final energy intensity by sector and fuel subelectricity subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic final energy intensity by sector and fuel subelectricity subhotels and restaurants':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subhotels_and_restaurants',
    'historic final energy intensity by sector and fuel subelectricity subinland transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subinland_transport',
    'historic final energy intensity by sector and fuel subelectricity subwater transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subwater_transport',
    'historic final energy intensity by sector and fuel subelectricity subair transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subair_transport',
    'historic final energy intensity by sector and fuel subelectricity subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic final energy intensity by sector and fuel subelectricity subpost and telecommunications':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subpost_and_telecommunications',
    'historic final energy intensity by sector and fuel subelectricity subfinancial intermediation':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subfinancial_intermediation',
    'historic final energy intensity by sector and fuel subelectricity subreal estate activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subreal_estate_activities',
    'historic final energy intensity by sector and fuel subelectricity subrenting od meq and other business activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subrenting_od_meq_and_other_business_activities',
    'historic final energy intensity by sector and fuel subelectricity subpublic admin and defence compulsory social security':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subpublic_admin_and_defence_compulsory_social_security',
    'historic final energy intensity by sector and fuel subelectricity subeducation':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subeducation',
    'historic final energy intensity by sector and fuel subelectricity subhealth and social work':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subhealth_and_social_work',
    'historic final energy intensity by sector and fuel subelectricity subother community social and persona services':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subother_community_social_and_persona_services',
    'historic final energy intensity by sector and fuel subelectricity subprivate households with employed persons':
    'historic_final_energy_intensity_by_sector_and_fuel_subelectricity_subprivate_households_with_employed_persons',
    'historic final energy intensity by sector and fuel subheat subagriculture hunting forestry and fishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subagriculture_hunting_forestry_and_fishing',
    'historic final energy intensity by sector and fuel subheat submining and quarrying':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_submining_and_quarrying',
    'historic final energy intensity by sector and fuel subheat subfood beverages and tobacco':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subfood_beverages_and_tobacco',
    'historic final energy intensity by sector and fuel subheat subtextiles and textile products':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subtextiles_and_textile_products',
    'historic final energy intensity by sector and fuel subheat subleather leather and footwear':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subleather_leather_and_footwear',
    'historic final energy intensity by sector and fuel subheat subwood and products of wood and cork':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subwood_and_products_of_wood_and_cork',
    'historic final energy intensity by sector and fuel subheat subpulp paper printing and publishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subpulp_paper_printing_and_publishing',
    'historic final energy intensity by sector and fuel subheat subcoke refined petroleum and nuclear fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic final energy intensity by sector and fuel subheat subchemicals and chemical products':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subchemicals_and_chemical_products',
    'historic final energy intensity by sector and fuel subheat subrubber and plastics':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subrubber_and_plastics',
    'historic final energy intensity by sector and fuel subheat subother non metalic mineral':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subother_non_metalic_mineral',
    'historic final energy intensity by sector and fuel subheat subbasic metals and fabricated metal':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subbasic_metals_and_fabricated_metal',
    'historic final energy intensity by sector and fuel subheat submachinery nec':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_submachinery_nec',
    'historic final energy intensity by sector and fuel subheat subelectrical and optical equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subelectrical_and_optical_equipment',
    'historic final energy intensity by sector and fuel subheat subtransport equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subtransport_equipment',
    'historic final energy intensity by sector and fuel subheat submanufacturing nec recycling':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_submanufacturing_nec_recycling',
    'historic final energy intensity by sector and fuel subheat subelectricity gas and water supply':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subelectricity_gas_and_water_supply',
    'historic final energy intensity by sector and fuel subheat subconstruction':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subconstruction',
    'historic final energy intensity by sector and fuel subheat subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic final energy intensity by sector and fuel subheat subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic final energy intensity by sector and fuel subheat subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic final energy intensity by sector and fuel subheat subhotels and restaurants':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subhotels_and_restaurants',
    'historic final energy intensity by sector and fuel subheat subinland transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subinland_transport',
    'historic final energy intensity by sector and fuel subheat subwater transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subwater_transport',
    'historic final energy intensity by sector and fuel subheat subair transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subair_transport',
    'historic final energy intensity by sector and fuel subheat subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic final energy intensity by sector and fuel subheat subpost and telecommunications':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subpost_and_telecommunications',
    'historic final energy intensity by sector and fuel subheat subfinancial intermediation':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subfinancial_intermediation',
    'historic final energy intensity by sector and fuel subheat subreal estate activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subreal_estate_activities',
    'historic final energy intensity by sector and fuel subheat subrenting od meq and other business activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subrenting_od_meq_and_other_business_activities',
    'historic final energy intensity by sector and fuel subheat subpublic admin and defence compulsory social security':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subpublic_admin_and_defence_compulsory_social_security',
    'historic final energy intensity by sector and fuel subheat subeducation':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subeducation',
    'historic final energy intensity by sector and fuel subheat subhealth and social work':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subhealth_and_social_work',
    'historic final energy intensity by sector and fuel subheat subother community social and persona services':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subother_community_social_and_persona_services',
    'historic final energy intensity by sector and fuel subheat subprivate households with employed persons':
    'historic_final_energy_intensity_by_sector_and_fuel_subheat_subprivate_households_with_employed_persons',
    'historic final energy intensity by sector and fuel subliquids subagriculture hunting forestry and fishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subagriculture_hunting_forestry_and_fishing',
    'historic final energy intensity by sector and fuel subliquids submining and quarrying':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_submining_and_quarrying',
    'historic final energy intensity by sector and fuel subliquids subfood beverages and tobacco':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subfood_beverages_and_tobacco',
    'historic final energy intensity by sector and fuel subliquids subtextiles and textile products':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subtextiles_and_textile_products',
    'historic final energy intensity by sector and fuel subliquids subleather leather and footwear':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subleather_leather_and_footwear',
    'historic final energy intensity by sector and fuel subliquids subwood and products of wood and cork':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subwood_and_products_of_wood_and_cork',
    'historic final energy intensity by sector and fuel subliquids subpulp paper printing and publishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subpulp_paper_printing_and_publishing',
    'historic final energy intensity by sector and fuel subliquids subcoke refined petroleum and nuclear fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic final energy intensity by sector and fuel subliquids subchemicals and chemical products':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subchemicals_and_chemical_products',
    'historic final energy intensity by sector and fuel subliquids subrubber and plastics':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subrubber_and_plastics',
    'historic final energy intensity by sector and fuel subliquids subother non metalic mineral':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subother_non_metalic_mineral',
    'historic final energy intensity by sector and fuel subliquids subbasic metals and fabricated metal':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subbasic_metals_and_fabricated_metal',
    'historic final energy intensity by sector and fuel subliquids submachinery nec':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_submachinery_nec',
    'historic final energy intensity by sector and fuel subliquids subelectrical and optical equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subelectrical_and_optical_equipment',
    'historic final energy intensity by sector and fuel subliquids subtransport equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subtransport_equipment',
    'historic final energy intensity by sector and fuel subliquids submanufacturing nec recycling':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_submanufacturing_nec_recycling',
    'historic final energy intensity by sector and fuel subliquids subelectricity gas and water supply':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subelectricity_gas_and_water_supply',
    'historic final energy intensity by sector and fuel subliquids subconstruction':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subconstruction',
    'historic final energy intensity by sector and fuel subliquids subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic final energy intensity by sector and fuel subliquids subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic final energy intensity by sector and fuel subliquids subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic final energy intensity by sector and fuel subliquids subhotels and restaurants':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subhotels_and_restaurants',
    'historic final energy intensity by sector and fuel subliquids subinland transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subinland_transport',
    'historic final energy intensity by sector and fuel subliquids subwater transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subwater_transport',
    'historic final energy intensity by sector and fuel subliquids subair transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subair_transport',
    'historic final energy intensity by sector and fuel subliquids subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic final energy intensity by sector and fuel subliquids subpost and telecommunications':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subpost_and_telecommunications',
    'historic final energy intensity by sector and fuel subliquids subfinancial intermediation':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subfinancial_intermediation',
    'historic final energy intensity by sector and fuel subliquids subreal estate activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subreal_estate_activities',
    'historic final energy intensity by sector and fuel subliquids subrenting od meq and other business activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subrenting_od_meq_and_other_business_activities',
    'historic final energy intensity by sector and fuel subliquids subpublic admin and defence compulsory social security':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subpublic_admin_and_defence_compulsory_social_security',
    'historic final energy intensity by sector and fuel subliquids subeducation':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subeducation',
    'historic final energy intensity by sector and fuel subliquids subhealth and social work':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subhealth_and_social_work',
    'historic final energy intensity by sector and fuel subliquids subother community social and persona services':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subother_community_social_and_persona_services',
    'historic final energy intensity by sector and fuel subliquids subprivate households with employed persons':
    'historic_final_energy_intensity_by_sector_and_fuel_subliquids_subprivate_households_with_employed_persons',
    'historic final energy intensity by sector and fuel subgases subagriculture hunting forestry and fishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subagriculture_hunting_forestry_and_fishing',
    'historic final energy intensity by sector and fuel subgases submining and quarrying':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_submining_and_quarrying',
    'historic final energy intensity by sector and fuel subgases subfood beverages and tobacco':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subfood_beverages_and_tobacco',
    'historic final energy intensity by sector and fuel subgases subtextiles and textile products':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subtextiles_and_textile_products',
    'historic final energy intensity by sector and fuel subgases subleather leather and footwear':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subleather_leather_and_footwear',
    'historic final energy intensity by sector and fuel subgases subwood and products of wood and cork':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subwood_and_products_of_wood_and_cork',
    'historic final energy intensity by sector and fuel subgases subpulp paper printing and publishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subpulp_paper_printing_and_publishing',
    'historic final energy intensity by sector and fuel subgases subcoke refined petroleum and nuclear fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic final energy intensity by sector and fuel subgases subchemicals and chemical products':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subchemicals_and_chemical_products',
    'historic final energy intensity by sector and fuel subgases subrubber and plastics':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subrubber_and_plastics',
    'historic final energy intensity by sector and fuel subgases subother non metalic mineral':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subother_non_metalic_mineral',
    'historic final energy intensity by sector and fuel subgases subbasic metals and fabricated metal':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subbasic_metals_and_fabricated_metal',
    'historic final energy intensity by sector and fuel subgases submachinery nec':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_submachinery_nec',
    'historic final energy intensity by sector and fuel subgases subelectrical and optical equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subelectrical_and_optical_equipment',
    'historic final energy intensity by sector and fuel subgases subtransport equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subtransport_equipment',
    'historic final energy intensity by sector and fuel subgases submanufacturing nec recycling':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_submanufacturing_nec_recycling',
    'historic final energy intensity by sector and fuel subgases subelectricity gas and water supply':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subelectricity_gas_and_water_supply',
    'historic final energy intensity by sector and fuel subgases subconstruction':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subconstruction',
    'historic final energy intensity by sector and fuel subgases subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic final energy intensity by sector and fuel subgases subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic final energy intensity by sector and fuel subgases subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic final energy intensity by sector and fuel subgases subhotels and restaurants':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subhotels_and_restaurants',
    'historic final energy intensity by sector and fuel subgases subinland transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subinland_transport',
    'historic final energy intensity by sector and fuel subgases subwater transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subwater_transport',
    'historic final energy intensity by sector and fuel subgases subair transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subair_transport',
    'historic final energy intensity by sector and fuel subgases subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic final energy intensity by sector and fuel subgases subpost and telecommunications':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subpost_and_telecommunications',
    'historic final energy intensity by sector and fuel subgases subfinancial intermediation':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subfinancial_intermediation',
    'historic final energy intensity by sector and fuel subgases subreal estate activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subreal_estate_activities',
    'historic final energy intensity by sector and fuel subgases subrenting od meq and other business activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subrenting_od_meq_and_other_business_activities',
    'historic final energy intensity by sector and fuel subgases subpublic admin and defence compulsory social security':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subpublic_admin_and_defence_compulsory_social_security',
    'historic final energy intensity by sector and fuel subgases subeducation':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subeducation',
    'historic final energy intensity by sector and fuel subgases subhealth and social work':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subhealth_and_social_work',
    'historic final energy intensity by sector and fuel subgases subother community social and persona services':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subother_community_social_and_persona_services',
    'historic final energy intensity by sector and fuel subgases subprivate households with employed persons':
    'historic_final_energy_intensity_by_sector_and_fuel_subgases_subprivate_households_with_employed_persons',
    'historic final energy intensity by sector and fuel subsolids subagriculture hunting forestry and fishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subagriculture_hunting_forestry_and_fishing',
    'historic final energy intensity by sector and fuel subsolids submining and quarrying':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_submining_and_quarrying',
    'historic final energy intensity by sector and fuel subsolids subfood beverages and tobacco':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subfood_beverages_and_tobacco',
    'historic final energy intensity by sector and fuel subsolids subtextiles and textile products':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subtextiles_and_textile_products',
    'historic final energy intensity by sector and fuel subsolids subleather leather and footwear':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subleather_leather_and_footwear',
    'historic final energy intensity by sector and fuel subsolids subwood and products of wood and cork':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subwood_and_products_of_wood_and_cork',
    'historic final energy intensity by sector and fuel subsolids subpulp paper printing and publishing':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subpulp_paper_printing_and_publishing',
    'historic final energy intensity by sector and fuel subsolids subcoke refined petroleum and nuclear fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic final energy intensity by sector and fuel subsolids subchemicals and chemical products':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subchemicals_and_chemical_products',
    'historic final energy intensity by sector and fuel subsolids subrubber and plastics':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subrubber_and_plastics',
    'historic final energy intensity by sector and fuel subsolids subother non metalic mineral':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subother_non_metalic_mineral',
    'historic final energy intensity by sector and fuel subsolids subbasic metals and fabricated metal':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subbasic_metals_and_fabricated_metal',
    'historic final energy intensity by sector and fuel subsolids submachinery nec':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_submachinery_nec',
    'historic final energy intensity by sector and fuel subsolids subelectrical and optical equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subelectrical_and_optical_equipment',
    'historic final energy intensity by sector and fuel subsolids subtransport equipment':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subtransport_equipment',
    'historic final energy intensity by sector and fuel subsolids submanufacturing nec recycling':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_submanufacturing_nec_recycling',
    'historic final energy intensity by sector and fuel subsolids subelectricity gas and water supply':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subelectricity_gas_and_water_supply',
    'historic final energy intensity by sector and fuel subsolids subconstruction':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subconstruction',
    'historic final energy intensity by sector and fuel subsolids subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic final energy intensity by sector and fuel subsolids subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic final energy intensity by sector and fuel subsolids subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic final energy intensity by sector and fuel subsolids subhotels and restaurants':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subhotels_and_restaurants',
    'historic final energy intensity by sector and fuel subsolids subinland transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subinland_transport',
    'historic final energy intensity by sector and fuel subsolids subwater transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subwater_transport',
    'historic final energy intensity by sector and fuel subsolids subair transport':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subair_transport',
    'historic final energy intensity by sector and fuel subsolids subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic final energy intensity by sector and fuel subsolids subpost and telecommunications':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subpost_and_telecommunications',
    'historic final energy intensity by sector and fuel subsolids subfinancial intermediation':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subfinancial_intermediation',
    'historic final energy intensity by sector and fuel subsolids subreal estate activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subreal_estate_activities',
    'historic final energy intensity by sector and fuel subsolids subrenting od meq and other business activities':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subrenting_od_meq_and_other_business_activities',
    'historic final energy intensity by sector and fuel subsolids subpublic admin and defence compulsory social security':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subpublic_admin_and_defence_compulsory_social_security',
    'historic final energy intensity by sector and fuel subsolids subeducation':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subeducation',
    'historic final energy intensity by sector and fuel subsolids subhealth and social work':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subhealth_and_social_work',
    'historic final energy intensity by sector and fuel subsolids subother community social and persona services':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subother_community_social_and_persona_services',
    'historic final energy intensity by sector and fuel subsolids subprivate households with employed persons':
    'historic_final_energy_intensity_by_sector_and_fuel_subsolids_subprivate_households_with_employed_persons',
    'historic final energy intensity h subelectricity':
    'historic_final_energy_intensity_h_subelectricity',
    'historic final energy intensity h subheat':
    'historic_final_energy_intensity_h_subheat',
    'historic final energy intensity h subliquids':
    'historic_final_energy_intensity_h_subliquids',
    'historic final energy intensity h subsolids':
    'historic_final_energy_intensity_h_subsolids',
    'historic final energy intensity h subgases':
    'historic_final_energy_intensity_h_subgases',
    'historic share gas div xcoal plus gasx for heat plants':
    'historic_share_gas_div_xcoal_plus_gasx_for_heat_plants',
    'hadcrut4 temperature':
    'hadcrut4_temperature',
    'co2 mauna loa':
    'co2_mauna_loa',
    'giss nasa temperature':
    'giss_nasa_temperature',
    'other forcings history':
    'other_forcings_history',
    'mp rf total':
    'mp_rf_total',
    'other forcings rcp scenario subrcp26':
    'other_forcings_rcp_scenario_subrcp26',
    'other forcings rcp scenario subrcp45':
    'other_forcings_rcp_scenario_subrcp45',
    'other forcings rcp scenario subrcp60':
    'other_forcings_rcp_scenario_subrcp60',
    'other forcings rcp scenario subrcp85':
    'other_forcings_rcp_scenario_subrcp85',
    'global sf6 emissions rcp subrcp26':
    'global_sf6_emissions_rcp_subrcp26',
    'global sf6 emissions rcp subrcp45':
    'global_sf6_emissions_rcp_subrcp45',
    'global sf6 emissions rcp subrcp60':
    'global_sf6_emissions_rcp_subrcp60',
    'global sf6 emissions rcp subrcp85':
    'global_sf6_emissions_rcp_subrcp85',
    'global ch4 anthro emissions rcp subrcp26':
    'global_ch4_anthro_emissions_rcp_subrcp26',
    'global ch4 anthro emissions rcp subrcp45':
    'global_ch4_anthro_emissions_rcp_subrcp45',
    'global ch4 anthro emissions rcp subrcp60':
    'global_ch4_anthro_emissions_rcp_subrcp60',
    'global ch4 anthro emissions rcp subrcp85':
    'global_ch4_anthro_emissions_rcp_subrcp85',
    'global hfc emissions rcp 26 subhfc134a':
    'global_hfc_emissions_rcp_26_subhfc134a',
    'global hfc emissions rcp 26 subhfc23':
    'global_hfc_emissions_rcp_26_subhfc23',
    'global hfc emissions rcp 26 subhfc32':
    'global_hfc_emissions_rcp_26_subhfc32',
    'global hfc emissions rcp 26 subhfc125':
    'global_hfc_emissions_rcp_26_subhfc125',
    'global hfc emissions rcp 26 subhfc143a':
    'global_hfc_emissions_rcp_26_subhfc143a',
    'global hfc emissions rcp 26 subhfc152a':
    'global_hfc_emissions_rcp_26_subhfc152a',
    'global hfc emissions rcp 26 subhfc227ea':
    'global_hfc_emissions_rcp_26_subhfc227ea',
    'global hfc emissions rcp 26 subhfc245ca':
    'global_hfc_emissions_rcp_26_subhfc245ca',
    'global hfc emissions rcp 26 subhfc4310mee':
    'global_hfc_emissions_rcp_26_subhfc4310mee',
    'global hfc emissions rcp 45 subhfc134a':
    'global_hfc_emissions_rcp_45_subhfc134a',
    'global hfc emissions rcp 45 subhfc23':
    'global_hfc_emissions_rcp_45_subhfc23',
    'global hfc emissions rcp 45 subhfc32':
    'global_hfc_emissions_rcp_45_subhfc32',
    'global hfc emissions rcp 45 subhfc125':
    'global_hfc_emissions_rcp_45_subhfc125',
    'global hfc emissions rcp 45 subhfc143a':
    'global_hfc_emissions_rcp_45_subhfc143a',
    'global hfc emissions rcp 45 subhfc152a':
    'global_hfc_emissions_rcp_45_subhfc152a',
    'global hfc emissions rcp 45 subhfc227ea':
    'global_hfc_emissions_rcp_45_subhfc227ea',
    'global hfc emissions rcp 45 subhfc245ca':
    'global_hfc_emissions_rcp_45_subhfc245ca',
    'global hfc emissions rcp 45 subhfc4310mee':
    'global_hfc_emissions_rcp_45_subhfc4310mee',
    'global hfc emissions rcp 60 subhfc134a':
    'global_hfc_emissions_rcp_60_subhfc134a',
    'global hfc emissions rcp 60 subhfc23':
    'global_hfc_emissions_rcp_60_subhfc23',
    'global hfc emissions rcp 60 subhfc32':
    'global_hfc_emissions_rcp_60_subhfc32',
    'global hfc emissions rcp 60 subhfc125':
    'global_hfc_emissions_rcp_60_subhfc125',
    'global hfc emissions rcp 60 subhfc143a':
    'global_hfc_emissions_rcp_60_subhfc143a',
    'global hfc emissions rcp 60 subhfc152a':
    'global_hfc_emissions_rcp_60_subhfc152a',
    'global hfc emissions rcp 60 subhfc227ea':
    'global_hfc_emissions_rcp_60_subhfc227ea',
    'global hfc emissions rcp 60 subhfc245ca':
    'global_hfc_emissions_rcp_60_subhfc245ca',
    'global hfc emissions rcp 60 subhfc4310mee':
    'global_hfc_emissions_rcp_60_subhfc4310mee',
    'global pfc emissions rcp subrcp26':
    'global_pfc_emissions_rcp_subrcp26',
    'global pfc emissions rcp subrcp45':
    'global_pfc_emissions_rcp_subrcp45',
    'global pfc emissions rcp subrcp60':
    'global_pfc_emissions_rcp_subrcp60',
    'global pfc emissions rcp subrcp85':
    'global_pfc_emissions_rcp_subrcp85',
    'global n2o anthro emissions rcp subrcp26':
    'global_n2o_anthro_emissions_rcp_subrcp26',
    'global n2o anthro emissions rcp subrcp45':
    'global_n2o_anthro_emissions_rcp_subrcp45',
    'global n2o anthro emissions rcp subrcp60':
    'global_n2o_anthro_emissions_rcp_subrcp60',
    'global n2o anthro emissions rcp subrcp85':
    'global_n2o_anthro_emissions_rcp_subrcp85',
    'global hfc emissions rcp 85 subhfc134a':
    'global_hfc_emissions_rcp_85_subhfc134a',
    'global hfc emissions rcp 85 subhfc23':
    'global_hfc_emissions_rcp_85_subhfc23',
    'global hfc emissions rcp 85 subhfc32':
    'global_hfc_emissions_rcp_85_subhfc32',
    'global hfc emissions rcp 85 subhfc125':
    'global_hfc_emissions_rcp_85_subhfc125',
    'global hfc emissions rcp 85 subhfc143a':
    'global_hfc_emissions_rcp_85_subhfc143a',
    'global hfc emissions rcp 85 subhfc152a':
    'global_hfc_emissions_rcp_85_subhfc152a',
    'global hfc emissions rcp 85 subhfc227ea':
    'global_hfc_emissions_rcp_85_subhfc227ea',
    'global hfc emissions rcp 85 subhfc245ca':
    'global_hfc_emissions_rcp_85_subhfc245ca',
    'global hfc emissions rcp 85 subhfc4310mee':
    'global_hfc_emissions_rcp_85_subhfc4310mee',
    'co2x land use change emissions exogenous':
    'co2x_land_use_change_emissions_exogenous',
    'historic water use by type sectors subagriculture hunting forestry and fishing subblue water':
    'historic_water_use_by_type_sectors_subagriculture_hunting_forestry_and_fishing_subblue_water',
    'historic water use by type sectors subagriculture hunting forestry and fishing subgreen water':
    'historic_water_use_by_type_sectors_subagriculture_hunting_forestry_and_fishing_subgreen_water',
    'historic water use by type sectors subagriculture hunting forestry and fishing subgray water':
    'historic_water_use_by_type_sectors_subagriculture_hunting_forestry_and_fishing_subgray_water',
    'historic water use by type sectors submining and quarrying subblue water':
    'historic_water_use_by_type_sectors_submining_and_quarrying_subblue_water',
    'historic water use by type sectors submining and quarrying subgreen water':
    'historic_water_use_by_type_sectors_submining_and_quarrying_subgreen_water',
    'historic water use by type sectors submining and quarrying subgray water':
    'historic_water_use_by_type_sectors_submining_and_quarrying_subgray_water',
    'historic water use by type sectors subfood beverages and tobacco subblue water':
    'historic_water_use_by_type_sectors_subfood_beverages_and_tobacco_subblue_water',
    'historic water use by type sectors subfood beverages and tobacco subgreen water':
    'historic_water_use_by_type_sectors_subfood_beverages_and_tobacco_subgreen_water',
    'historic water use by type sectors subfood beverages and tobacco subgray water':
    'historic_water_use_by_type_sectors_subfood_beverages_and_tobacco_subgray_water',
    'historic water use by type sectors subtextiles and textile products subblue water':
    'historic_water_use_by_type_sectors_subtextiles_and_textile_products_subblue_water',
    'historic water use by type sectors subtextiles and textile products subgreen water':
    'historic_water_use_by_type_sectors_subtextiles_and_textile_products_subgreen_water',
    'historic water use by type sectors subtextiles and textile products subgray water':
    'historic_water_use_by_type_sectors_subtextiles_and_textile_products_subgray_water',
    'historic water use by type sectors subleather leather and footwear subblue water':
    'historic_water_use_by_type_sectors_subleather_leather_and_footwear_subblue_water',
    'historic water use by type sectors subleather leather and footwear subgreen water':
    'historic_water_use_by_type_sectors_subleather_leather_and_footwear_subgreen_water',
    'historic water use by type sectors subleather leather and footwear subgray water':
    'historic_water_use_by_type_sectors_subleather_leather_and_footwear_subgray_water',
    'historic water use by type sectors subwood and products of wood and cork subblue water':
    'historic_water_use_by_type_sectors_subwood_and_products_of_wood_and_cork_subblue_water',
    'historic water use by type sectors subwood and products of wood and cork subgreen water':
    'historic_water_use_by_type_sectors_subwood_and_products_of_wood_and_cork_subgreen_water',
    'historic water use by type sectors subwood and products of wood and cork subgray water':
    'historic_water_use_by_type_sectors_subwood_and_products_of_wood_and_cork_subgray_water',
    'historic water use by type sectors subpulp paper printing and publishing subblue water':
    'historic_water_use_by_type_sectors_subpulp_paper_printing_and_publishing_subblue_water',
    'historic water use by type sectors subpulp paper printing and publishing subgreen water':
    'historic_water_use_by_type_sectors_subpulp_paper_printing_and_publishing_subgreen_water',
    'historic water use by type sectors subpulp paper printing and publishing subgray water':
    'historic_water_use_by_type_sectors_subpulp_paper_printing_and_publishing_subgray_water',
    'historic water use by type sectors subcoke refined petroleum and nuclear fuel subblue water':
    'historic_water_use_by_type_sectors_subcoke_refined_petroleum_and_nuclear_fuel_subblue_water',
    'historic water use by type sectors subcoke refined petroleum and nuclear fuel subgreen water':
    'historic_water_use_by_type_sectors_subcoke_refined_petroleum_and_nuclear_fuel_subgreen_water',
    'historic water use by type sectors subcoke refined petroleum and nuclear fuel subgray water':
    'historic_water_use_by_type_sectors_subcoke_refined_petroleum_and_nuclear_fuel_subgray_water',
    'historic water use by type sectors subchemicals and chemical products subblue water':
    'historic_water_use_by_type_sectors_subchemicals_and_chemical_products_subblue_water',
    'historic water use by type sectors subchemicals and chemical products subgreen water':
    'historic_water_use_by_type_sectors_subchemicals_and_chemical_products_subgreen_water',
    'historic water use by type sectors subchemicals and chemical products subgray water':
    'historic_water_use_by_type_sectors_subchemicals_and_chemical_products_subgray_water',
    'historic water use by type sectors subrubber and plastics subblue water':
    'historic_water_use_by_type_sectors_subrubber_and_plastics_subblue_water',
    'historic water use by type sectors subrubber and plastics subgreen water':
    'historic_water_use_by_type_sectors_subrubber_and_plastics_subgreen_water',
    'historic water use by type sectors subrubber and plastics subgray water':
    'historic_water_use_by_type_sectors_subrubber_and_plastics_subgray_water',
    'historic water use by type sectors subother non metalic mineral subblue water':
    'historic_water_use_by_type_sectors_subother_non_metalic_mineral_subblue_water',
    'historic water use by type sectors subother non metalic mineral subgreen water':
    'historic_water_use_by_type_sectors_subother_non_metalic_mineral_subgreen_water',
    'historic water use by type sectors subother non metalic mineral subgray water':
    'historic_water_use_by_type_sectors_subother_non_metalic_mineral_subgray_water',
    'historic water use by type sectors subbasic metals and fabricated metal subblue water':
    'historic_water_use_by_type_sectors_subbasic_metals_and_fabricated_metal_subblue_water',
    'historic water use by type sectors subbasic metals and fabricated metal subgreen water':
    'historic_water_use_by_type_sectors_subbasic_metals_and_fabricated_metal_subgreen_water',
    'historic water use by type sectors subbasic metals and fabricated metal subgray water':
    'historic_water_use_by_type_sectors_subbasic_metals_and_fabricated_metal_subgray_water',
    'historic water use by type sectors submachinery nec subblue water':
    'historic_water_use_by_type_sectors_submachinery_nec_subblue_water',
    'historic water use by type sectors submachinery nec subgreen water':
    'historic_water_use_by_type_sectors_submachinery_nec_subgreen_water',
    'historic water use by type sectors submachinery nec subgray water':
    'historic_water_use_by_type_sectors_submachinery_nec_subgray_water',
    'historic water use by type sectors subelectrical and optical equipment subblue water':
    'historic_water_use_by_type_sectors_subelectrical_and_optical_equipment_subblue_water',
    'historic water use by type sectors subelectrical and optical equipment subgreen water':
    'historic_water_use_by_type_sectors_subelectrical_and_optical_equipment_subgreen_water',
    'historic water use by type sectors subelectrical and optical equipment subgray water':
    'historic_water_use_by_type_sectors_subelectrical_and_optical_equipment_subgray_water',
    'historic water use by type sectors subtransport equipment subblue water':
    'historic_water_use_by_type_sectors_subtransport_equipment_subblue_water',
    'historic water use by type sectors subtransport equipment subgreen water':
    'historic_water_use_by_type_sectors_subtransport_equipment_subgreen_water',
    'historic water use by type sectors subtransport equipment subgray water':
    'historic_water_use_by_type_sectors_subtransport_equipment_subgray_water',
    'historic water use by type sectors submanufacturing nec recycling subblue water':
    'historic_water_use_by_type_sectors_submanufacturing_nec_recycling_subblue_water',
    'historic water use by type sectors submanufacturing nec recycling subgreen water':
    'historic_water_use_by_type_sectors_submanufacturing_nec_recycling_subgreen_water',
    'historic water use by type sectors submanufacturing nec recycling subgray water':
    'historic_water_use_by_type_sectors_submanufacturing_nec_recycling_subgray_water',
    'historic water use by type sectors subelectricity gas and water supply subblue water':
    'historic_water_use_by_type_sectors_subelectricity_gas_and_water_supply_subblue_water',
    'historic water use by type sectors subelectricity gas and water supply subgreen water':
    'historic_water_use_by_type_sectors_subelectricity_gas_and_water_supply_subgreen_water',
    'historic water use by type sectors subelectricity gas and water supply subgray water':
    'historic_water_use_by_type_sectors_subelectricity_gas_and_water_supply_subgray_water',
    'historic water use by type sectors subconstruction subblue water':
    'historic_water_use_by_type_sectors_subconstruction_subblue_water',
    'historic water use by type sectors subconstruction subgreen water':
    'historic_water_use_by_type_sectors_subconstruction_subgreen_water',
    'historic water use by type sectors subconstruction subgray water':
    'historic_water_use_by_type_sectors_subconstruction_subgray_water',
    'historic water use by type sectors subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel subblue water':
    'historic_water_use_by_type_sectors_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel_subblue_water',
    'historic water use by type sectors subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel subgreen water':
    'historic_water_use_by_type_sectors_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel_subgreen_water',
    'historic water use by type sectors subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel subgray water':
    'historic_water_use_by_type_sectors_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel_subgray_water',
    'historic water use by type sectors subwholesale trade and commissions trade except of motor vehicles and motorcycles subblue water':
    'historic_water_use_by_type_sectors_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles_subblue_water',
    'historic water use by type sectors subwholesale trade and commissions trade except of motor vehicles and motorcycles subgreen water':
    'historic_water_use_by_type_sectors_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles_subgreen_water',
    'historic water use by type sectors subwholesale trade and commissions trade except of motor vehicles and motorcycles subgray water':
    'historic_water_use_by_type_sectors_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles_subgray_water',
    'historic water use by type sectors subretail trade except of motor vehicles and motorcycles repair of household goods subblue water':
    'historic_water_use_by_type_sectors_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods_subblue_water',
    'historic water use by type sectors subretail trade except of motor vehicles and motorcycles repair of household goods subgreen water':
    'historic_water_use_by_type_sectors_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods_subgreen_water',
    'historic water use by type sectors subretail trade except of motor vehicles and motorcycles repair of household goods subgray water':
    'historic_water_use_by_type_sectors_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods_subgray_water',
    'historic water use by type sectors subhotels and restaurants subblue water':
    'historic_water_use_by_type_sectors_subhotels_and_restaurants_subblue_water',
    'historic water use by type sectors subhotels and restaurants subgreen water':
    'historic_water_use_by_type_sectors_subhotels_and_restaurants_subgreen_water',
    'historic water use by type sectors subhotels and restaurants subgray water':
    'historic_water_use_by_type_sectors_subhotels_and_restaurants_subgray_water',
    'historic water use by type sectors subinland transport subblue water':
    'historic_water_use_by_type_sectors_subinland_transport_subblue_water',
    'historic water use by type sectors subinland transport subgreen water':
    'historic_water_use_by_type_sectors_subinland_transport_subgreen_water',
    'historic water use by type sectors subinland transport subgray water':
    'historic_water_use_by_type_sectors_subinland_transport_subgray_water',
    'historic water use by type sectors subwater transport subblue water':
    'historic_water_use_by_type_sectors_subwater_transport_subblue_water',
    'historic water use by type sectors subwater transport subgreen water':
    'historic_water_use_by_type_sectors_subwater_transport_subgreen_water',
    'historic water use by type sectors subwater transport subgray water':
    'historic_water_use_by_type_sectors_subwater_transport_subgray_water',
    'historic water use by type sectors subair transport subblue water':
    'historic_water_use_by_type_sectors_subair_transport_subblue_water',
    'historic water use by type sectors subair transport subgreen water':
    'historic_water_use_by_type_sectors_subair_transport_subgreen_water',
    'historic water use by type sectors subair transport subgray water':
    'historic_water_use_by_type_sectors_subair_transport_subgray_water',
    'historic water use by type sectors subother supporting and auxiliary transport activities activities of travel agencies subblue water':
    'historic_water_use_by_type_sectors_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies_subblue_water',
    'historic water use by type sectors subother supporting and auxiliary transport activities activities of travel agencies subgreen water':
    'historic_water_use_by_type_sectors_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies_subgreen_water',
    'historic water use by type sectors subother supporting and auxiliary transport activities activities of travel agencies subgray water':
    'historic_water_use_by_type_sectors_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies_subgray_water',
    'historic water use by type sectors subpost and telecommunications subblue water':
    'historic_water_use_by_type_sectors_subpost_and_telecommunications_subblue_water',
    'historic water use by type sectors subpost and telecommunications subgreen water':
    'historic_water_use_by_type_sectors_subpost_and_telecommunications_subgreen_water',
    'historic water use by type sectors subpost and telecommunications subgray water':
    'historic_water_use_by_type_sectors_subpost_and_telecommunications_subgray_water',
    'historic water use by type sectors subfinancial intermediation subblue water':
    'historic_water_use_by_type_sectors_subfinancial_intermediation_subblue_water',
    'historic water use by type sectors subfinancial intermediation subgreen water':
    'historic_water_use_by_type_sectors_subfinancial_intermediation_subgreen_water',
    'historic water use by type sectors subfinancial intermediation subgray water':
    'historic_water_use_by_type_sectors_subfinancial_intermediation_subgray_water',
    'historic water use by type sectors subreal estate activities subblue water':
    'historic_water_use_by_type_sectors_subreal_estate_activities_subblue_water',
    'historic water use by type sectors subreal estate activities subgreen water':
    'historic_water_use_by_type_sectors_subreal_estate_activities_subgreen_water',
    'historic water use by type sectors subreal estate activities subgray water':
    'historic_water_use_by_type_sectors_subreal_estate_activities_subgray_water',
    'historic water use by type sectors subrenting od meq and other business activities subblue water':
    'historic_water_use_by_type_sectors_subrenting_od_meq_and_other_business_activities_subblue_water',
    'historic water use by type sectors subrenting od meq and other business activities subgreen water':
    'historic_water_use_by_type_sectors_subrenting_od_meq_and_other_business_activities_subgreen_water',
    'historic water use by type sectors subrenting od meq and other business activities subgray water':
    'historic_water_use_by_type_sectors_subrenting_od_meq_and_other_business_activities_subgray_water',
    'historic water use by type sectors subpublic admin and defence compulsory social security subblue water':
    'historic_water_use_by_type_sectors_subpublic_admin_and_defence_compulsory_social_security_subblue_water',
    'historic water use by type sectors subpublic admin and defence compulsory social security subgreen water':
    'historic_water_use_by_type_sectors_subpublic_admin_and_defence_compulsory_social_security_subgreen_water',
    'historic water use by type sectors subpublic admin and defence compulsory social security subgray water':
    'historic_water_use_by_type_sectors_subpublic_admin_and_defence_compulsory_social_security_subgray_water',
    'historic water use by type sectors subeducation subblue water':
    'historic_water_use_by_type_sectors_subeducation_subblue_water',
    'historic water use by type sectors subeducation subgreen water':
    'historic_water_use_by_type_sectors_subeducation_subgreen_water',
    'historic water use by type sectors subeducation subgray water':
    'historic_water_use_by_type_sectors_subeducation_subgray_water',
    'historic water use by type sectors subhealth and social work subblue water':
    'historic_water_use_by_type_sectors_subhealth_and_social_work_subblue_water',
    'historic water use by type sectors subhealth and social work subgreen water':
    'historic_water_use_by_type_sectors_subhealth_and_social_work_subgreen_water',
    'historic water use by type sectors subhealth and social work subgray water':
    'historic_water_use_by_type_sectors_subhealth_and_social_work_subgray_water',
    'historic water use by type sectors subother community social and persona services subblue water':
    'historic_water_use_by_type_sectors_subother_community_social_and_persona_services_subblue_water',
    'historic water use by type sectors subother community social and persona services subgreen water':
    'historic_water_use_by_type_sectors_subother_community_social_and_persona_services_subgreen_water',
    'historic water use by type sectors subother community social and persona services subgray water':
    'historic_water_use_by_type_sectors_subother_community_social_and_persona_services_subgray_water',
    'historic water use by type sectors subprivate households with employed persons subblue water':
    'historic_water_use_by_type_sectors_subprivate_households_with_employed_persons_subblue_water',
    'historic water use by type sectors subprivate households with employed persons subgreen water':
    'historic_water_use_by_type_sectors_subprivate_households_with_employed_persons_subgreen_water',
    'historic water use by type sectors subprivate households with employed persons subgray water':
    'historic_water_use_by_type_sectors_subprivate_households_with_employed_persons_subgray_water',
    'historic water use by type for households subblue water':
    'historic_water_use_by_type_for_households_subblue_water',
    'historic water use by type for households subgreen water':
    'historic_water_use_by_type_for_households_subgreen_water',
    'historic water use by type for households subgray water':
    'historic_water_use_by_type_for_households_subgray_water',
    'gdppc annual growth ssp2':
    'gdppc_annual_growth_ssp2',
    'pop ssp2':
    'pop_ssp2',
    'pop ssp4':
    'pop_ssp4',
    'pop ssp1':
    'pop_ssp1',
    'pop ssp5':
    'pop_ssp5',
    'pop ssp3':
    'pop_ssp3',
    'p timeseries gdppc growth rate':
    'p_timeseries_gdppc_growth_rate',
    'historic gdppc':
    'historic_gdppc',
    'total ghg emissions olt medeas d3x2':
    'total_ghg_emissions_olt_medeas_d3x2',
    'total ghg emissions bau cat medeas d3x2':
    'total_ghg_emissions_bau_cat_medeas_d3x2',
    'total ghg emissions mlt2030x medeas d3x2':
    'total_ghg_emissions_mlt2030x_medeas_d3x2',
    'total ghg emissions mlt2020x medeas d3x2':
    'total_ghg_emissions_mlt2020x_medeas_d3x2',
    'table hist capacity phs':
    'table_hist_capacity_phs',
    'table max extraction aspo oil ej 0 1 0':
    'table_max_extraction_aspo_oil_ej_0_1_0',
    'table max extraction aspo oil ej 0 1':
    'table_max_extraction_aspo_oil_ej_0_1',
    'table max extraction aspo oil ej 0':
    'table_max_extraction_aspo_oil_ej_0',
    'table max extraction aspo oil ej 0 0':
    'table_max_extraction_aspo_oil_ej_0_0',
    'historical extraction minerals rest subadhesive':
    'historical_extraction_minerals_rest_subadhesive',
    'historical extraction minerals rest subaluminium':
    'historical_extraction_minerals_rest_subaluminium',
    'historical extraction minerals rest subaluminium mirrors':
    'historical_extraction_minerals_rest_subaluminium_mirrors',
    'historical extraction minerals rest subcadmium':
    'historical_extraction_minerals_rest_subcadmium',
    'historical extraction minerals rest subcarbon fiber':
    'historical_extraction_minerals_rest_subcarbon_fiber',
    'historical extraction minerals rest subcement':
    'historical_extraction_minerals_rest_subcement',
    'historical extraction minerals rest subchromium':
    'historical_extraction_minerals_rest_subchromium',
    'historical extraction minerals rest subcopper':
    'historical_extraction_minerals_rest_subcopper',
    'historical extraction minerals rest subdiesel':
    'historical_extraction_minerals_rest_subdiesel',
    'historical extraction minerals rest subdy':
    'historical_extraction_minerals_rest_subdy',
    'historical extraction minerals rest subelectric div electronic components':
    'historical_extraction_minerals_rest_subelectric_div_electronic_components',
    'historical extraction minerals rest subevacuation lines':
    'historical_extraction_minerals_rest_subevacuation_lines',
    'historical extraction minerals rest subfiberglass':
    'historical_extraction_minerals_rest_subfiberglass',
    'historical extraction minerals rest subfoam glass':
    'historical_extraction_minerals_rest_subfoam_glass',
    'historical extraction minerals rest subgalium':
    'historical_extraction_minerals_rest_subgalium',
    'historical extraction minerals rest subglass':
    'historical_extraction_minerals_rest_subglass',
    'historical extraction minerals rest subglass reinforcing plastic':
    'historical_extraction_minerals_rest_subglass_reinforcing_plastic',
    'historical extraction minerals rest subgravel':
    'historical_extraction_minerals_rest_subgravel',
    'historical extraction minerals rest subindium':
    'historical_extraction_minerals_rest_subindium',
    'historical extraction minerals rest subiron':
    'historical_extraction_minerals_rest_subiron',
    'historical extraction minerals rest subkno3 mined':
    'historical_extraction_minerals_rest_subkno3_mined',
    'historical extraction minerals rest subasphalt':
    'historical_extraction_minerals_rest_subasphalt',
    'historical extraction minerals rest sublime':
    'historical_extraction_minerals_rest_sublime',
    'historical extraction minerals rest sublimestone':
    'historical_extraction_minerals_rest_sublimestone',
    'historical extraction minerals rest sublithium':
    'historical_extraction_minerals_rest_sublithium',
    'historical extraction minerals rest sublubricant':
    'historical_extraction_minerals_rest_sublubricant',
    'historical extraction minerals rest submagnesium':
    'historical_extraction_minerals_rest_submagnesium',
    'historical extraction minerals rest submanganese':
    'historical_extraction_minerals_rest_submanganese',
    'historical extraction minerals rest subheavy equipment':
    'historical_extraction_minerals_rest_subheavy_equipment',
    'historical extraction minerals rest subconcrete':
    'historical_extraction_minerals_rest_subconcrete',
    'historical extraction minerals rest submolybdenum':
    'historical_extraction_minerals_rest_submolybdenum',
    'historical extraction minerals rest subnano3 mined':
    'historical_extraction_minerals_rest_subnano3_mined',
    'historical extraction minerals rest subnano3 synthetic':
    'historical_extraction_minerals_rest_subnano3_synthetic',
    'historical extraction minerals rest subneodymium':
    'historical_extraction_minerals_rest_subneodymium',
    'historical extraction minerals rest subnickel':
    'historical_extraction_minerals_rest_subnickel',
    'historical extraction minerals rest subover grid 15 percentx':
    'historical_extraction_minerals_rest_subover_grid_15_percentx',
    'historical extraction minerals rest subover grid 5 percentx':
    'historical_extraction_minerals_rest_subover_grid_5_percentx',
    'historical extraction minerals rest subpaint':
    'historical_extraction_minerals_rest_subpaint',
    'historical extraction minerals rest sublead':
    'historical_extraction_minerals_rest_sublead',
    'historical extraction minerals rest subplastics':
    'historical_extraction_minerals_rest_subplastics',
    'historical extraction minerals rest subpolypropylene':
    'historical_extraction_minerals_rest_subpolypropylene',
    'historical extraction minerals rest subrock':
    'historical_extraction_minerals_rest_subrock',
    'historical extraction minerals rest subrock wool':
    'historical_extraction_minerals_rest_subrock_wool',
    'historical extraction minerals rest subsand':
    'historical_extraction_minerals_rest_subsand',
    'historical extraction minerals rest subsilicon sand':
    'historical_extraction_minerals_rest_subsilicon_sand',
    'historical extraction minerals rest subsilicon wafer modules':
    'historical_extraction_minerals_rest_subsilicon_wafer_modules',
    'historical extraction minerals rest subsilver':
    'historical_extraction_minerals_rest_subsilver',
    'historical extraction minerals rest subsite preparation':
    'historical_extraction_minerals_rest_subsite_preparation',
    'historical extraction minerals rest subtin':
    'historical_extraction_minerals_rest_subtin',
    'historical extraction minerals rest subsoda ash':
    'historical_extraction_minerals_rest_subsoda_ash',
    'historical extraction minerals rest substeel':
    'historical_extraction_minerals_rest_substeel',
    'historical extraction minerals rest subsynthetic oil':
    'historical_extraction_minerals_rest_subsynthetic_oil',
    'historical extraction minerals rest subtellurium':
    'historical_extraction_minerals_rest_subtellurium',
    'historical extraction minerals rest subtitanium':
    'historical_extraction_minerals_rest_subtitanium',
    'historical extraction minerals rest subtitanium dioxide':
    'historical_extraction_minerals_rest_subtitanium_dioxide',
    'historical extraction minerals rest subvanadium':
    'historical_extraction_minerals_rest_subvanadium',
    'historical extraction minerals rest subwires':
    'historical_extraction_minerals_rest_subwires',
    'historical extraction minerals rest subzinc':
    'historical_extraction_minerals_rest_subzinc',
    'start production biofuels':
    'start_production_biofuels',
    'historic res capacity for heat nc subsolar heat':
    'historic_res_capacity_for_heat_nc_subsolar_heat',
    'historic res capacity for heat nc subgeot heat':
    'historic_res_capacity_for_heat_nc_subgeot_heat',
    'historic res capacity for heat nc subsolid bioe heat':
    'historic_res_capacity_for_heat_nc_subsolid_bioe_heat',
    'historic share of transformation losses vs extraction subliquids':
    'historic_share_of_transformation_losses_vs_extraction_subliquids',
    'historic share of transformation losses vs extraction subsolids':
    'historic_share_of_transformation_losses_vs_extraction_subsolids',
    'ratio gain gas vs lose solids in tranf processes':
    'ratio_gain_gas_vs_lose_solids_in_tranf_processes',
    'historic share of losses vs extraction subliquids':
    'historic_share_of_losses_vs_extraction_subliquids',
    'historic share of losses vs extraction subsolids':
    'historic_share_of_losses_vs_extraction_subsolids',
    'historic share of losses vs extraction subgases':
    'historic_share_of_losses_vs_extraction_subgases',
    'historic demand by sector subagriculture hunting forestry and fishing':
    'historic_demand_by_sector_subagriculture_hunting_forestry_and_fishing',
    'historic demand by sector submining and quarrying':
    'historic_demand_by_sector_submining_and_quarrying',
    'historic demand by sector subfood beverages and tobacco':
    'historic_demand_by_sector_subfood_beverages_and_tobacco',
    'historic demand by sector subtextiles and textile products':
    'historic_demand_by_sector_subtextiles_and_textile_products',
    'historic demand by sector subleather leather and footwear':
    'historic_demand_by_sector_subleather_leather_and_footwear',
    'historic demand by sector subwood and products of wood and cork':
    'historic_demand_by_sector_subwood_and_products_of_wood_and_cork',
    'historic demand by sector subpulp paper printing and publishing':
    'historic_demand_by_sector_subpulp_paper_printing_and_publishing',
    'historic demand by sector subcoke refined petroleum and nuclear fuel':
    'historic_demand_by_sector_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic demand by sector subchemicals and chemical products':
    'historic_demand_by_sector_subchemicals_and_chemical_products',
    'historic demand by sector subrubber and plastics':
    'historic_demand_by_sector_subrubber_and_plastics',
    'historic demand by sector subother non metalic mineral':
    'historic_demand_by_sector_subother_non_metalic_mineral',
    'historic demand by sector subbasic metals and fabricated metal':
    'historic_demand_by_sector_subbasic_metals_and_fabricated_metal',
    'historic demand by sector submachinery nec':
    'historic_demand_by_sector_submachinery_nec',
    'historic demand by sector subelectrical and optical equipment':
    'historic_demand_by_sector_subelectrical_and_optical_equipment',
    'historic demand by sector subtransport equipment':
    'historic_demand_by_sector_subtransport_equipment',
    'historic demand by sector submanufacturing nec recycling':
    'historic_demand_by_sector_submanufacturing_nec_recycling',
    'historic demand by sector subelectricity gas and water supply':
    'historic_demand_by_sector_subelectricity_gas_and_water_supply',
    'historic demand by sector subconstruction':
    'historic_demand_by_sector_subconstruction',
    'historic demand by sector subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_demand_by_sector_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic demand by sector subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_demand_by_sector_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic demand by sector subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_demand_by_sector_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic demand by sector subhotels and restaurants':
    'historic_demand_by_sector_subhotels_and_restaurants',
    'historic demand by sector subinland transport':
    'historic_demand_by_sector_subinland_transport',
    'historic demand by sector subwater transport':
    'historic_demand_by_sector_subwater_transport',
    'historic demand by sector subair transport':
    'historic_demand_by_sector_subair_transport',
    'historic demand by sector subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_demand_by_sector_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic demand by sector subpost and telecommunications':
    'historic_demand_by_sector_subpost_and_telecommunications',
    'historic demand by sector subfinancial intermediation':
    'historic_demand_by_sector_subfinancial_intermediation',
    'historic demand by sector subreal estate activities':
    'historic_demand_by_sector_subreal_estate_activities',
    'historic demand by sector subrenting od meq and other business activities':
    'historic_demand_by_sector_subrenting_od_meq_and_other_business_activities',
    'historic demand by sector subpublic admin and defence compulsory social security':
    'historic_demand_by_sector_subpublic_admin_and_defence_compulsory_social_security',
    'historic demand by sector subeducation':
    'historic_demand_by_sector_subeducation',
    'historic demand by sector subhealth and social work':
    'historic_demand_by_sector_subhealth_and_social_work',
    'historic demand by sector subother community social and persona services':
    'historic_demand_by_sector_subother_community_social_and_persona_services',
    'historic demand by sector subprivate households with employed persons':
    'historic_demand_by_sector_subprivate_households_with_employed_persons',
    'historic res capacity for heat com subsolar heat':
    'historic_res_capacity_for_heat_com_subsolar_heat',
    'historic res capacity for heat com subgeot heat':
    'historic_res_capacity_for_heat_com_subgeot_heat',
    'historic res capacity for heat com subsolid bioe heat':
    'historic_res_capacity_for_heat_com_subsolid_bioe_heat',
    'share inventories next step subagriculture hunting forestry and fishing':
    'share_inventories_next_step_subagriculture_hunting_forestry_and_fishing',
    'share inventories next step submining and quarrying':
    'share_inventories_next_step_submining_and_quarrying',
    'share inventories next step subfood beverages and tobacco':
    'share_inventories_next_step_subfood_beverages_and_tobacco',
    'share inventories next step subtextiles and textile products':
    'share_inventories_next_step_subtextiles_and_textile_products',
    'share inventories next step subleather leather and footwear':
    'share_inventories_next_step_subleather_leather_and_footwear',
    'share inventories next step subwood and products of wood and cork':
    'share_inventories_next_step_subwood_and_products_of_wood_and_cork',
    'share inventories next step subpulp paper printing and publishing':
    'share_inventories_next_step_subpulp_paper_printing_and_publishing',
    'share inventories next step subcoke refined petroleum and nuclear fuel':
    'share_inventories_next_step_subcoke_refined_petroleum_and_nuclear_fuel',
    'share inventories next step subchemicals and chemical products':
    'share_inventories_next_step_subchemicals_and_chemical_products',
    'share inventories next step subrubber and plastics':
    'share_inventories_next_step_subrubber_and_plastics',
    'share inventories next step subother non metalic mineral':
    'share_inventories_next_step_subother_non_metalic_mineral',
    'share inventories next step subbasic metals and fabricated metal':
    'share_inventories_next_step_subbasic_metals_and_fabricated_metal',
    'share inventories next step submachinery nec':
    'share_inventories_next_step_submachinery_nec',
    'share inventories next step subelectrical and optical equipment':
    'share_inventories_next_step_subelectrical_and_optical_equipment',
    'share inventories next step subtransport equipment':
    'share_inventories_next_step_subtransport_equipment',
    'share inventories next step submanufacturing nec recycling':
    'share_inventories_next_step_submanufacturing_nec_recycling',
    'share inventories next step subelectricity gas and water supply':
    'share_inventories_next_step_subelectricity_gas_and_water_supply',
    'share inventories next step subconstruction':
    'share_inventories_next_step_subconstruction',
    'share inventories next step subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'share_inventories_next_step_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'share inventories next step subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'share_inventories_next_step_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'share inventories next step subretail trade except of motor vehicles and motorcycles repair of household goods':
    'share_inventories_next_step_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'share inventories next step subhotels and restaurants':
    'share_inventories_next_step_subhotels_and_restaurants',
    'share inventories next step subinland transport':
    'share_inventories_next_step_subinland_transport',
    'share inventories next step subwater transport':
    'share_inventories_next_step_subwater_transport',
    'share inventories next step subair transport':
    'share_inventories_next_step_subair_transport',
    'share inventories next step subother supporting and auxiliary transport activities activities of travel agencies':
    'share_inventories_next_step_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'share inventories next step subpost and telecommunications':
    'share_inventories_next_step_subpost_and_telecommunications',
    'share inventories next step subfinancial intermediation':
    'share_inventories_next_step_subfinancial_intermediation',
    'share inventories next step subreal estate activities':
    'share_inventories_next_step_subreal_estate_activities',
    'share inventories next step subrenting od meq and other business activities':
    'share_inventories_next_step_subrenting_od_meq_and_other_business_activities',
    'share inventories next step subpublic admin and defence compulsory social security':
    'share_inventories_next_step_subpublic_admin_and_defence_compulsory_social_security',
    'share inventories next step subeducation':
    'share_inventories_next_step_subeducation',
    'share inventories next step subhealth and social work':
    'share_inventories_next_step_subhealth_and_social_work',
    'share inventories next step subother community social and persona services':
    'share_inventories_next_step_subother_community_social_and_persona_services',
    'share inventories next step subprivate households with employed persons':
    'share_inventories_next_step_subprivate_households_with_employed_persons',
    'share consum goverments subagriculture hunting forestry and fishing':
    'share_consum_goverments_subagriculture_hunting_forestry_and_fishing',
    'share consum goverments submining and quarrying':
    'share_consum_goverments_submining_and_quarrying',
    'share consum goverments subfood beverages and tobacco':
    'share_consum_goverments_subfood_beverages_and_tobacco',
    'share consum goverments subtextiles and textile products':
    'share_consum_goverments_subtextiles_and_textile_products',
    'share consum goverments subleather leather and footwear':
    'share_consum_goverments_subleather_leather_and_footwear',
    'share consum goverments subwood and products of wood and cork':
    'share_consum_goverments_subwood_and_products_of_wood_and_cork',
    'share consum goverments subpulp paper printing and publishing':
    'share_consum_goverments_subpulp_paper_printing_and_publishing',
    'share consum goverments subcoke refined petroleum and nuclear fuel':
    'share_consum_goverments_subcoke_refined_petroleum_and_nuclear_fuel',
    'share consum goverments subchemicals and chemical products':
    'share_consum_goverments_subchemicals_and_chemical_products',
    'share consum goverments subrubber and plastics':
    'share_consum_goverments_subrubber_and_plastics',
    'share consum goverments subother non metalic mineral':
    'share_consum_goverments_subother_non_metalic_mineral',
    'share consum goverments subbasic metals and fabricated metal':
    'share_consum_goverments_subbasic_metals_and_fabricated_metal',
    'share consum goverments submachinery nec':
    'share_consum_goverments_submachinery_nec',
    'share consum goverments subelectrical and optical equipment':
    'share_consum_goverments_subelectrical_and_optical_equipment',
    'share consum goverments subtransport equipment':
    'share_consum_goverments_subtransport_equipment',
    'share consum goverments submanufacturing nec recycling':
    'share_consum_goverments_submanufacturing_nec_recycling',
    'share consum goverments subelectricity gas and water supply':
    'share_consum_goverments_subelectricity_gas_and_water_supply',
    'share consum goverments subconstruction':
    'share_consum_goverments_subconstruction',
    'share consum goverments subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'share_consum_goverments_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'share consum goverments subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'share_consum_goverments_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'share consum goverments subretail trade except of motor vehicles and motorcycles repair of household goods':
    'share_consum_goverments_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'share consum goverments subhotels and restaurants':
    'share_consum_goverments_subhotels_and_restaurants',
    'share consum goverments subinland transport':
    'share_consum_goverments_subinland_transport',
    'share consum goverments subwater transport':
    'share_consum_goverments_subwater_transport',
    'share consum goverments subair transport':
    'share_consum_goverments_subair_transport',
    'share consum goverments subother supporting and auxiliary transport activities activities of travel agencies':
    'share_consum_goverments_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'share consum goverments subpost and telecommunications':
    'share_consum_goverments_subpost_and_telecommunications',
    'share consum goverments subfinancial intermediation':
    'share_consum_goverments_subfinancial_intermediation',
    'share consum goverments subreal estate activities':
    'share_consum_goverments_subreal_estate_activities',
    'share consum goverments subrenting od meq and other business activities':
    'share_consum_goverments_subrenting_od_meq_and_other_business_activities',
    'share consum goverments subpublic admin and defence compulsory social security':
    'share_consum_goverments_subpublic_admin_and_defence_compulsory_social_security',
    'share consum goverments subeducation':
    'share_consum_goverments_subeducation',
    'share consum goverments subhealth and social work':
    'share_consum_goverments_subhealth_and_social_work',
    'share consum goverments subother community social and persona services':
    'share_consum_goverments_subother_community_social_and_persona_services',
    'share consum goverments subprivate households with employed persons':
    'share_consum_goverments_subprivate_households_with_employed_persons',
    'share inventories subagriculture hunting forestry and fishing':
    'share_inventories_subagriculture_hunting_forestry_and_fishing',
    'share inventories submining and quarrying':
    'share_inventories_submining_and_quarrying',
    'share inventories subfood beverages and tobacco':
    'share_inventories_subfood_beverages_and_tobacco',
    'share inventories subtextiles and textile products':
    'share_inventories_subtextiles_and_textile_products',
    'share inventories subleather leather and footwear':
    'share_inventories_subleather_leather_and_footwear',
    'share inventories subwood and products of wood and cork':
    'share_inventories_subwood_and_products_of_wood_and_cork',
    'share inventories subpulp paper printing and publishing':
    'share_inventories_subpulp_paper_printing_and_publishing',
    'share inventories subcoke refined petroleum and nuclear fuel':
    'share_inventories_subcoke_refined_petroleum_and_nuclear_fuel',
    'share inventories subchemicals and chemical products':
    'share_inventories_subchemicals_and_chemical_products',
    'share inventories subrubber and plastics':
    'share_inventories_subrubber_and_plastics',
    'share inventories subother non metalic mineral':
    'share_inventories_subother_non_metalic_mineral',
    'share inventories subbasic metals and fabricated metal':
    'share_inventories_subbasic_metals_and_fabricated_metal',
    'share inventories submachinery nec':
    'share_inventories_submachinery_nec',
    'share inventories subelectrical and optical equipment':
    'share_inventories_subelectrical_and_optical_equipment',
    'share inventories subtransport equipment':
    'share_inventories_subtransport_equipment',
    'share inventories submanufacturing nec recycling':
    'share_inventories_submanufacturing_nec_recycling',
    'share inventories subelectricity gas and water supply':
    'share_inventories_subelectricity_gas_and_water_supply',
    'share inventories subconstruction':
    'share_inventories_subconstruction',
    'share inventories subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'share_inventories_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'share inventories subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'share_inventories_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'share inventories subretail trade except of motor vehicles and motorcycles repair of household goods':
    'share_inventories_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'share inventories subhotels and restaurants':
    'share_inventories_subhotels_and_restaurants',
    'share inventories subinland transport':
    'share_inventories_subinland_transport',
    'share inventories subwater transport':
    'share_inventories_subwater_transport',
    'share inventories subair transport':
    'share_inventories_subair_transport',
    'share inventories subother supporting and auxiliary transport activities activities of travel agencies':
    'share_inventories_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'share inventories subpost and telecommunications':
    'share_inventories_subpost_and_telecommunications',
    'share inventories subfinancial intermediation':
    'share_inventories_subfinancial_intermediation',
    'share inventories subreal estate activities':
    'share_inventories_subreal_estate_activities',
    'share inventories subrenting od meq and other business activities':
    'share_inventories_subrenting_od_meq_and_other_business_activities',
    'share inventories subpublic admin and defence compulsory social security':
    'share_inventories_subpublic_admin_and_defence_compulsory_social_security',
    'share inventories subeducation':
    'share_inventories_subeducation',
    'share inventories subhealth and social work':
    'share_inventories_subhealth_and_social_work',
    'share inventories subother community social and persona services':
    'share_inventories_subother_community_social_and_persona_services',
    'share inventories subprivate households with employed persons':
    'share_inventories_subprivate_households_with_employed_persons',
    'share consum goverments next step subagriculture hunting forestry and fishing':
    'share_consum_goverments_next_step_subagriculture_hunting_forestry_and_fishing',
    'share consum goverments next step submining and quarrying':
    'share_consum_goverments_next_step_submining_and_quarrying',
    'share consum goverments next step subfood beverages and tobacco':
    'share_consum_goverments_next_step_subfood_beverages_and_tobacco',
    'share consum goverments next step subtextiles and textile products':
    'share_consum_goverments_next_step_subtextiles_and_textile_products',
    'share consum goverments next step subleather leather and footwear':
    'share_consum_goverments_next_step_subleather_leather_and_footwear',
    'share consum goverments next step subwood and products of wood and cork':
    'share_consum_goverments_next_step_subwood_and_products_of_wood_and_cork',
    'share consum goverments next step subpulp paper printing and publishing':
    'share_consum_goverments_next_step_subpulp_paper_printing_and_publishing',
    'share consum goverments next step subcoke refined petroleum and nuclear fuel':
    'share_consum_goverments_next_step_subcoke_refined_petroleum_and_nuclear_fuel',
    'share consum goverments next step subchemicals and chemical products':
    'share_consum_goverments_next_step_subchemicals_and_chemical_products',
    'share consum goverments next step subrubber and plastics':
    'share_consum_goverments_next_step_subrubber_and_plastics',
    'share consum goverments next step subother non metalic mineral':
    'share_consum_goverments_next_step_subother_non_metalic_mineral',
    'share consum goverments next step subbasic metals and fabricated metal':
    'share_consum_goverments_next_step_subbasic_metals_and_fabricated_metal',
    'share consum goverments next step submachinery nec':
    'share_consum_goverments_next_step_submachinery_nec',
    'share consum goverments next step subelectrical and optical equipment':
    'share_consum_goverments_next_step_subelectrical_and_optical_equipment',
    'share consum goverments next step subtransport equipment':
    'share_consum_goverments_next_step_subtransport_equipment',
    'share consum goverments next step submanufacturing nec recycling':
    'share_consum_goverments_next_step_submanufacturing_nec_recycling',
    'share consum goverments next step subelectricity gas and water supply':
    'share_consum_goverments_next_step_subelectricity_gas_and_water_supply',
    'share consum goverments next step subconstruction':
    'share_consum_goverments_next_step_subconstruction',
    'share consum goverments next step subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'share_consum_goverments_next_step_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'share consum goverments next step subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'share_consum_goverments_next_step_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'share consum goverments next step subretail trade except of motor vehicles and motorcycles repair of household goods':
    'share_consum_goverments_next_step_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'share consum goverments next step subhotels and restaurants':
    'share_consum_goverments_next_step_subhotels_and_restaurants',
    'share consum goverments next step subinland transport':
    'share_consum_goverments_next_step_subinland_transport',
    'share consum goverments next step subwater transport':
    'share_consum_goverments_next_step_subwater_transport',
    'share consum goverments next step subair transport':
    'share_consum_goverments_next_step_subair_transport',
    'share consum goverments next step subother supporting and auxiliary transport activities activities of travel agencies':
    'share_consum_goverments_next_step_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'share consum goverments next step subpost and telecommunications':
    'share_consum_goverments_next_step_subpost_and_telecommunications',
    'share consum goverments next step subfinancial intermediation':
    'share_consum_goverments_next_step_subfinancial_intermediation',
    'share consum goverments next step subreal estate activities':
    'share_consum_goverments_next_step_subreal_estate_activities',
    'share consum goverments next step subrenting od meq and other business activities':
    'share_consum_goverments_next_step_subrenting_od_meq_and_other_business_activities',
    'share consum goverments next step subpublic admin and defence compulsory social security':
    'share_consum_goverments_next_step_subpublic_admin_and_defence_compulsory_social_security',
    'share consum goverments next step subeducation':
    'share_consum_goverments_next_step_subeducation',
    'share consum goverments next step subhealth and social work':
    'share_consum_goverments_next_step_subhealth_and_social_work',
    'share consum goverments next step subother community social and persona services':
    'share_consum_goverments_next_step_subother_community_social_and_persona_services',
    'share consum goverments next step subprivate households with employed persons':
    'share_consum_goverments_next_step_subprivate_households_with_employed_persons',
    'historic gfcf subagriculture hunting forestry and fishing':
    'historic_gfcf_subagriculture_hunting_forestry_and_fishing',
    'historic gfcf submining and quarrying':
    'historic_gfcf_submining_and_quarrying',
    'historic gfcf subfood beverages and tobacco':
    'historic_gfcf_subfood_beverages_and_tobacco',
    'historic gfcf subtextiles and textile products':
    'historic_gfcf_subtextiles_and_textile_products',
    'historic gfcf subleather leather and footwear':
    'historic_gfcf_subleather_leather_and_footwear',
    'historic gfcf subwood and products of wood and cork':
    'historic_gfcf_subwood_and_products_of_wood_and_cork',
    'historic gfcf subpulp paper printing and publishing':
    'historic_gfcf_subpulp_paper_printing_and_publishing',
    'historic gfcf subcoke refined petroleum and nuclear fuel':
    'historic_gfcf_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic gfcf subchemicals and chemical products':
    'historic_gfcf_subchemicals_and_chemical_products',
    'historic gfcf subrubber and plastics':
    'historic_gfcf_subrubber_and_plastics',
    'historic gfcf subother non metalic mineral':
    'historic_gfcf_subother_non_metalic_mineral',
    'historic gfcf subbasic metals and fabricated metal':
    'historic_gfcf_subbasic_metals_and_fabricated_metal',
    'historic gfcf submachinery nec':
    'historic_gfcf_submachinery_nec',
    'historic gfcf subelectrical and optical equipment':
    'historic_gfcf_subelectrical_and_optical_equipment',
    'historic gfcf subtransport equipment':
    'historic_gfcf_subtransport_equipment',
    'historic gfcf submanufacturing nec recycling':
    'historic_gfcf_submanufacturing_nec_recycling',
    'historic gfcf subelectricity gas and water supply':
    'historic_gfcf_subelectricity_gas_and_water_supply',
    'historic gfcf subconstruction':
    'historic_gfcf_subconstruction',
    'historic gfcf subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_gfcf_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic gfcf subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_gfcf_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic gfcf subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_gfcf_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic gfcf subhotels and restaurants':
    'historic_gfcf_subhotels_and_restaurants',
    'historic gfcf subinland transport':
    'historic_gfcf_subinland_transport',
    'historic gfcf subwater transport':
    'historic_gfcf_subwater_transport',
    'historic gfcf subair transport':
    'historic_gfcf_subair_transport',
    'historic gfcf subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_gfcf_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic gfcf subpost and telecommunications':
    'historic_gfcf_subpost_and_telecommunications',
    'historic gfcf subfinancial intermediation':
    'historic_gfcf_subfinancial_intermediation',
    'historic gfcf subreal estate activities':
    'historic_gfcf_subreal_estate_activities',
    'historic gfcf subrenting od meq and other business activities':
    'historic_gfcf_subrenting_od_meq_and_other_business_activities',
    'historic gfcf subpublic admin and defence compulsory social security':
    'historic_gfcf_subpublic_admin_and_defence_compulsory_social_security',
    'historic gfcf subeducation':
    'historic_gfcf_subeducation',
    'historic gfcf subhealth and social work':
    'historic_gfcf_subhealth_and_social_work',
    'historic gfcf subother community social and persona services':
    'historic_gfcf_subother_community_social_and_persona_services',
    'historic gfcf subprivate households with employed persons':
    'historic_gfcf_subprivate_households_with_employed_persons',
    'historic hd subagriculture hunting forestry and fishing':
    'historic_hd_subagriculture_hunting_forestry_and_fishing',
    'historic hd submining and quarrying':
    'historic_hd_submining_and_quarrying',
    'historic hd subfood beverages and tobacco':
    'historic_hd_subfood_beverages_and_tobacco',
    'historic hd subtextiles and textile products':
    'historic_hd_subtextiles_and_textile_products',
    'historic hd subleather leather and footwear':
    'historic_hd_subleather_leather_and_footwear',
    'historic hd subwood and products of wood and cork':
    'historic_hd_subwood_and_products_of_wood_and_cork',
    'historic hd subpulp paper printing and publishing':
    'historic_hd_subpulp_paper_printing_and_publishing',
    'historic hd subcoke refined petroleum and nuclear fuel':
    'historic_hd_subcoke_refined_petroleum_and_nuclear_fuel',
    'historic hd subchemicals and chemical products':
    'historic_hd_subchemicals_and_chemical_products',
    'historic hd subrubber and plastics':
    'historic_hd_subrubber_and_plastics',
    'historic hd subother non metalic mineral':
    'historic_hd_subother_non_metalic_mineral',
    'historic hd subbasic metals and fabricated metal':
    'historic_hd_subbasic_metals_and_fabricated_metal',
    'historic hd submachinery nec':
    'historic_hd_submachinery_nec',
    'historic hd subelectrical and optical equipment':
    'historic_hd_subelectrical_and_optical_equipment',
    'historic hd subtransport equipment':
    'historic_hd_subtransport_equipment',
    'historic hd submanufacturing nec recycling':
    'historic_hd_submanufacturing_nec_recycling',
    'historic hd subelectricity gas and water supply':
    'historic_hd_subelectricity_gas_and_water_supply',
    'historic hd subconstruction':
    'historic_hd_subconstruction',
    'historic hd subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'historic_hd_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'historic hd subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'historic_hd_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'historic hd subretail trade except of motor vehicles and motorcycles repair of household goods':
    'historic_hd_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'historic hd subhotels and restaurants':
    'historic_hd_subhotels_and_restaurants',
    'historic hd subinland transport':
    'historic_hd_subinland_transport',
    'historic hd subwater transport':
    'historic_hd_subwater_transport',
    'historic hd subair transport':
    'historic_hd_subair_transport',
    'historic hd subother supporting and auxiliary transport activities activities of travel agencies':
    'historic_hd_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'historic hd subpost and telecommunications':
    'historic_hd_subpost_and_telecommunications',
    'historic hd subfinancial intermediation':
    'historic_hd_subfinancial_intermediation',
    'historic hd subreal estate activities':
    'historic_hd_subreal_estate_activities',
    'historic hd subrenting od meq and other business activities':
    'historic_hd_subrenting_od_meq_and_other_business_activities',
    'historic hd subpublic admin and defence compulsory social security':
    'historic_hd_subpublic_admin_and_defence_compulsory_social_security',
    'historic hd subeducation':
    'historic_hd_subeducation',
    'historic hd subhealth and social work':
    'historic_hd_subhealth_and_social_work',
    'historic hd subother community social and persona services':
    'historic_hd_subother_community_social_and_persona_services',
    'historic hd subprivate households with employed persons':
    'historic_hd_subprivate_households_with_employed_persons',
    'share cc next step subagriculture hunting forestry and fishing':
    'share_cc_next_step_subagriculture_hunting_forestry_and_fishing',
    'share cc next step submining and quarrying':
    'share_cc_next_step_submining_and_quarrying',
    'share cc next step subfood beverages and tobacco':
    'share_cc_next_step_subfood_beverages_and_tobacco',
    'share cc next step subtextiles and textile products':
    'share_cc_next_step_subtextiles_and_textile_products',
    'share cc next step subleather leather and footwear':
    'share_cc_next_step_subleather_leather_and_footwear',
    'share cc next step subwood and products of wood and cork':
    'share_cc_next_step_subwood_and_products_of_wood_and_cork',
    'share cc next step subpulp paper printing and publishing':
    'share_cc_next_step_subpulp_paper_printing_and_publishing',
    'share cc next step subcoke refined petroleum and nuclear fuel':
    'share_cc_next_step_subcoke_refined_petroleum_and_nuclear_fuel',
    'share cc next step subchemicals and chemical products':
    'share_cc_next_step_subchemicals_and_chemical_products',
    'share cc next step subrubber and plastics':
    'share_cc_next_step_subrubber_and_plastics',
    'share cc next step subother non metalic mineral':
    'share_cc_next_step_subother_non_metalic_mineral',
    'share cc next step subbasic metals and fabricated metal':
    'share_cc_next_step_subbasic_metals_and_fabricated_metal',
    'share cc next step submachinery nec':
    'share_cc_next_step_submachinery_nec',
    'share cc next step subelectrical and optical equipment':
    'share_cc_next_step_subelectrical_and_optical_equipment',
    'share cc next step subtransport equipment':
    'share_cc_next_step_subtransport_equipment',
    'share cc next step submanufacturing nec recycling':
    'share_cc_next_step_submanufacturing_nec_recycling',
    'share cc next step subelectricity gas and water supply':
    'share_cc_next_step_subelectricity_gas_and_water_supply',
    'share cc next step subconstruction':
    'share_cc_next_step_subconstruction',
    'share cc next step subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'share_cc_next_step_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'share cc next step subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'share_cc_next_step_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'share cc next step subretail trade except of motor vehicles and motorcycles repair of household goods':
    'share_cc_next_step_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'share cc next step subhotels and restaurants':
    'share_cc_next_step_subhotels_and_restaurants',
    'share cc next step subinland transport':
    'share_cc_next_step_subinland_transport',
    'share cc next step subwater transport':
    'share_cc_next_step_subwater_transport',
    'share cc next step subair transport':
    'share_cc_next_step_subair_transport',
    'share cc next step subother supporting and auxiliary transport activities activities of travel agencies':
    'share_cc_next_step_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'share cc next step subpost and telecommunications':
    'share_cc_next_step_subpost_and_telecommunications',
    'share cc next step subfinancial intermediation':
    'share_cc_next_step_subfinancial_intermediation',
    'share cc next step subreal estate activities':
    'share_cc_next_step_subreal_estate_activities',
    'share cc next step subrenting od meq and other business activities':
    'share_cc_next_step_subrenting_od_meq_and_other_business_activities',
    'share cc next step subpublic admin and defence compulsory social security':
    'share_cc_next_step_subpublic_admin_and_defence_compulsory_social_security',
    'share cc next step subeducation':
    'share_cc_next_step_subeducation',
    'share cc next step subhealth and social work':
    'share_cc_next_step_subhealth_and_social_work',
    'share cc next step subother community social and persona services':
    'share_cc_next_step_subother_community_social_and_persona_services',
    'share cc next step subprivate households with employed persons':
    'share_cc_next_step_subprivate_households_with_employed_persons',
    'historic labour share':
    'historic_labour_share',
    'share cc sectoral subagriculture hunting forestry and fishing':
    'share_cc_sectoral_subagriculture_hunting_forestry_and_fishing',
    'share cc sectoral submining and quarrying':
    'share_cc_sectoral_submining_and_quarrying',
    'share cc sectoral subfood beverages and tobacco':
    'share_cc_sectoral_subfood_beverages_and_tobacco',
    'share cc sectoral subtextiles and textile products':
    'share_cc_sectoral_subtextiles_and_textile_products',
    'share cc sectoral subleather leather and footwear':
    'share_cc_sectoral_subleather_leather_and_footwear',
    'share cc sectoral subwood and products of wood and cork':
    'share_cc_sectoral_subwood_and_products_of_wood_and_cork',
    'share cc sectoral subpulp paper printing and publishing':
    'share_cc_sectoral_subpulp_paper_printing_and_publishing',
    'share cc sectoral subcoke refined petroleum and nuclear fuel':
    'share_cc_sectoral_subcoke_refined_petroleum_and_nuclear_fuel',
    'share cc sectoral subchemicals and chemical products':
    'share_cc_sectoral_subchemicals_and_chemical_products',
    'share cc sectoral subrubber and plastics':
    'share_cc_sectoral_subrubber_and_plastics',
    'share cc sectoral subother non metalic mineral':
    'share_cc_sectoral_subother_non_metalic_mineral',
    'share cc sectoral subbasic metals and fabricated metal':
    'share_cc_sectoral_subbasic_metals_and_fabricated_metal',
    'share cc sectoral submachinery nec':
    'share_cc_sectoral_submachinery_nec',
    'share cc sectoral subelectrical and optical equipment':
    'share_cc_sectoral_subelectrical_and_optical_equipment',
    'share cc sectoral subtransport equipment':
    'share_cc_sectoral_subtransport_equipment',
    'share cc sectoral submanufacturing nec recycling':
    'share_cc_sectoral_submanufacturing_nec_recycling',
    'share cc sectoral subelectricity gas and water supply':
    'share_cc_sectoral_subelectricity_gas_and_water_supply',
    'share cc sectoral subconstruction':
    'share_cc_sectoral_subconstruction',
    'share cc sectoral subsale maintenance and repair of motor vehicles anda motorcycles retail sale of fuel':
    'share_cc_sectoral_subsale_maintenance_and_repair_of_motor_vehicles_anda_motorcycles_retail_sale_of_fuel',
    'share cc sectoral subwholesale trade and commissions trade except of motor vehicles and motorcycles':
    'share_cc_sectoral_subwholesale_trade_and_commissions_trade_except_of_motor_vehicles_and_motorcycles',
    'share cc sectoral subretail trade except of motor vehicles and motorcycles repair of household goods':
    'share_cc_sectoral_subretail_trade_except_of_motor_vehicles_and_motorcycles_repair_of_household_goods',
    'share cc sectoral subhotels and restaurants':
    'share_cc_sectoral_subhotels_and_restaurants',
    'share cc sectoral subinland transport':
    'share_cc_sectoral_subinland_transport',
    'share cc sectoral subwater transport':
    'share_cc_sectoral_subwater_transport',
    'share cc sectoral subair transport':
    'share_cc_sectoral_subair_transport',
    'share cc sectoral subother supporting and auxiliary transport activities activities of travel agencies':
    'share_cc_sectoral_subother_supporting_and_auxiliary_transport_activities_activities_of_travel_agencies',
    'share cc sectoral subpost and telecommunications':
    'share_cc_sectoral_subpost_and_telecommunications',
    'share cc sectoral subfinancial intermediation':
    'share_cc_sectoral_subfinancial_intermediation',
    'share cc sectoral subreal estate activities':
    'share_cc_sectoral_subreal_estate_activities',
    'share cc sectoral subrenting od meq and other business activities':
    'share_cc_sectoral_subrenting_od_meq_and_other_business_activities',
    'share cc sectoral subpublic admin and defence compulsory social security':
    'share_cc_sectoral_subpublic_admin_and_defence_compulsory_social_security',
    'share cc sectoral subeducation':
    'share_cc_sectoral_subeducation',
    'share cc sectoral subhealth and social work':
    'share_cc_sectoral_subhealth_and_social_work',
    'share cc sectoral subother community social and persona services':
    'share_cc_sectoral_subother_community_social_and_persona_services',
    'share cc sectoral subprivate households with employed persons':
    'share_cc_sectoral_subprivate_households_with_employed_persons',
    'historic pes waste ej':
    'historic_pes_waste_ej',
    'table hist capacity res elec subhydro':
    'table_hist_capacity_res_elec_subhydro',
    'table hist capacity res elec subgeot elec':
    'table_hist_capacity_res_elec_subgeot_elec',
    'table hist capacity res elec subsolid bioe elec':
    'table_hist_capacity_res_elec_subsolid_bioe_elec',
    'table hist capacity res elec suboceanic':
    'table_hist_capacity_res_elec_suboceanic',
    'table hist capacity res elec subwind onshore':
    'table_hist_capacity_res_elec_subwind_onshore',
    'table hist capacity res elec subwind offshore':
    'table_hist_capacity_res_elec_subwind_offshore',
    'table hist capacity res elec subsolar pv':
    'table_hist_capacity_res_elec_subsolar_pv',
    'table hist capacity res elec subcsp':
    'table_hist_capacity_res_elec_subcsp',
    'losses in charcoal plants ej':
    'losses_in_charcoal_plants_ej',
    'historic share chp plants gas':
    'historic_share_chp_plants_gas',
    'historic share liquids for heat plants':
    'historic_share_liquids_for_heat_plants',
    'historic share chp plants oil':
    'historic_share_chp_plants_oil',
    'historic biogas pes':
    'historic_biogas_pes',
    'historic pes peat ej':
    'historic_pes_peat_ej',
    'efficiency heat oil chp plants':
    'efficiency_heat_oil_chp_plants',
    'efficiency elec coal chp plants':
    'efficiency_elec_coal_chp_plants',
    'efficiency elec gas chp plants':
    'efficiency_elec_gas_chp_plants',
    'efficiency elec oil chp plants':
    'efficiency_elec_oil_chp_plants',
    'efficiency heat gas chp plants':
    'efficiency_heat_gas_chp_plants',
    'share heat com chp plants nre vs nre tot heat com generation':
    'share_heat_com_chp_plants_nre_vs_nre_tot_heat_com_generation',
    'efficiency heat coal chp plants':
    'efficiency_heat_coal_chp_plants',
    'historic non energy use subliquids':
    'historic_non_energy_use_subliquids',
    'historic non energy use subsolids':
    'historic_non_energy_use_subsolids',
    'historic non energy use subgases':
    'historic_non_energy_use_subgases',
    'historic non energy use subelectricity':
    'historic_non_energy_use_subelectricity',
    'historic non energy use subheat':
    'historic_non_energy_use_subheat',
    'efficiency liquids for heat plants':
    'efficiency_liquids_for_heat_plants',
    'efficiency coal for heat plants':
    'efficiency_coal_for_heat_plants',
    'efficiency gases for heat plants':
    'efficiency_gases_for_heat_plants',
    'invest cost res elec subhydro':
    'invest_cost_res_elec_subhydro',
    'invest cost res elec subgeot elec':
    'invest_cost_res_elec_subgeot_elec',
    'invest cost res elec subsolid bioe elec':
    'invest_cost_res_elec_subsolid_bioe_elec',
    'invest cost res elec suboceanic':
    'invest_cost_res_elec_suboceanic',
    'invest cost res elec subwind onshore':
    'invest_cost_res_elec_subwind_onshore',
    'invest cost res elec subwind offshore':
    'invest_cost_res_elec_subwind_offshore',
    'invest cost res elec subsolar pv':
    'invest_cost_res_elec_subsolar_pv',
    'invest cost res elec subcsp':
    'invest_cost_res_elec_subcsp',
    'table max extraction uranium user defined':
    'table_max_extraction_uranium_user_defined',
    'user defined extraction growth unconv gas':
    'user_defined_extraction_growth_unconv_gas',
    'user defined extraction growth unconv oil':
    'user_defined_extraction_growth_unconv_oil',
    'historic unconv oil':
    'historic_unconv_oil',
    'historic unconv gas':
    'historic_unconv_gas',
    'historic pop':
    'historic_pop',
    'balancing costs ref':
    'balancing_costs_ref',
    'historic gtl production':
    'historic_gtl_production',
    'historic ctl production':
    'historic_ctl_production',
    'historic produc biofuels 2gen':
    'historic_produc_biofuels_2gen',
    'table max extraction tot agg oil laherrere 2006':
    'table_max_extraction_tot_agg_oil_laherrere_2006',
    'table max extraction maggio12 high conv oil ej':
    'table_max_extraction_maggio12_high_conv_oil_ej',
    'table max extraction maggio12 low con oil ej':
    'table_max_extraction_maggio12_low_con_oil_ej',
    'table max extraction maggio12middle conv oil ej':
    'table_max_extraction_maggio12middle_conv_oil_ej',
    'table max extraction unconv oil user defined':
    'table_max_extraction_unconv_oil_user_defined',
    'table max extraction uranium zittel12':
    'table_max_extraction_uranium_zittel12',
    'table max extraction unconv oil low mohr15':
    'table_max_extraction_unconv_oil_low_mohr15',
    'table max extraction unconv oil high mohr15':
    'table_max_extraction_unconv_oil_high_mohr15',
    'table max extraction tot agg oil user defined':
    'table_max_extraction_tot_agg_oil_user_defined',
    'table max conv oil extraction user defined':
    'table_max_conv_oil_extraction_user_defined',
    'table max extraction uranium ewg13 ej':
    'table_max_extraction_uranium_ewg13_ej',
    'hist share oil div ff elec':
    'hist_share_oil_div_ff_elec',
    'hist share gas div xcoal plus gasx elec':
    'hist_share_gas_div_xcoal_plus_gasx_elec',
    'historic nuclear generation twh':
    'historic_nuclear_generation_twh',
    'invest cost nuclear':
    'invest_cost_nuclear',
    'tpes de castro phd scen xmadcoalx':
    'tpes_de_castro_phd_scen_xmadcoalx',
    'gtc historic emissions rcps':
    'gtc_historic_emissions_rcps',
    'afforestation program 2020':
    'afforestation_program_2020',
    'historic efficiency gas for electricity':
    'historic_efficiency_gas_for_electricity',
    'p timeseries pop growth rate':
    'p_timeseries_pop_growth_rate',
    'time dmnl':
    'time_dmnl',
    'table max extraction aspo oil ej':
    'table_max_extraction_aspo_oil_ej',
    'table max extraction gas laherrere2010':
    'table_max_extraction_gas_laherrere2010',
    'table max extraction gas mohr high2012':
    'table_max_extraction_gas_mohr_high2012',
    'table max extraction gas mohr bg2012':
    'table_max_extraction_gas_mohr_bg2012',
    'tnes de castro phd scen i':
    'tnes_de_castro_phd_scen_i',
    'net oil extraction de castro phd scen i':
    'net_oil_extraction_de_castro_phd_scen_i',
    'pe oil extraction de castro phd scen ii':
    'pe_oil_extraction_de_castro_phd_scen_ii',
    'net oil extraction de castro phd scen iii':
    'net_oil_extraction_de_castro_phd_scen_iii',
    'pe coal extraction de castro phd scen ii':
    'pe_coal_extraction_de_castro_phd_scen_ii',
    'net gas extraction de castro phd scen i':
    'net_gas_extraction_de_castro_phd_scen_i',
    'pe gas extraction de castro phd scen ii':
    'pe_gas_extraction_de_castro_phd_scen_ii',
    'net gas extraction de castro phd scen iii':
    'net_gas_extraction_de_castro_phd_scen_iii',
    'net coal extraction de castro phd scen iii':
    'net_coal_extraction_de_castro_phd_scen_iii',
    'net coal extraction de castro phd scen i':
    'net_coal_extraction_de_castro_phd_scen_i',
    'tnes de castro phd scen iii':
    'tnes_de_castro_phd_scen_iii',
    'primary coal extraction de castro phd scen xmadcoalx':
    'primary_coal_extraction_de_castro_phd_scen_xmadcoalx',
    'tpes de castro phd scen ii':
    'tpes_de_castro_phd_scen_ii',
    'table max extraction conv gas low mohr15':
    'table_max_extraction_conv_gas_low_mohr15',
    'table max extraction conv gas user defined':
    'table_max_extraction_conv_gas_user_defined',
    'table max extraction total gas bg mohr12':
    'table_max_extraction_total_gas_bg_mohr12',
    'table max extraction total gas laherrere10':
    'table_max_extraction_total_gas_laherrere10',
    'table max extraction total gas user defined':
    'table_max_extraction_total_gas_user_defined',
    'table max extraction unconv gas bg mohr15':
    'table_max_extraction_unconv_gas_bg_mohr15',
    'table max extraction unconv gas high mohr15':
    'table_max_extraction_unconv_gas_high_mohr15',
    'table max extraction unconv gas low mohr15':
    'table_max_extraction_unconv_gas_low_mohr15',
    'table max extraction unconv gas user defined':
    'table_max_extraction_unconv_gas_user_defined',
    'table max extraction coal bg mohr15':
    'table_max_extraction_coal_bg_mohr15',
    'table max extraction coal high mohr15':
    'table_max_extraction_coal_high_mohr15',
    'table max extraction coal low mohr15':
    'table_max_extraction_coal_low_mohr15',
    'table max extraction coal mohr2012 ej':
    'table_max_extraction_coal_mohr2012_ej',
    'table max extraction coal user defined':
    'table_max_extraction_coal_user_defined',
    'table max extraction conv gas bg mohr15':
    'table_max_extraction_conv_gas_bg_mohr15',
    'table max extraction conv gas high mohr15':
    'table_max_extraction_conv_gas_high_mohr15',
    'table max extraction unconv oil bg mohr15':
    'table_max_extraction_unconv_oil_bg_mohr15',
    'year energy intensity target':
    'year_energy_intensity_target',
    'policy to improve efficiency speed':
    'policy_to_improve_efficiency_speed',
    'start year modification ei':
    'start_year_modification_ei',
    'share biogas in pes':
    'share_biogas_in_pes',
    'fes total biogas':
    'fes_total_biogas',
    'fes total biofuels':
    'fes_total_biofuels',
    'share biofuel in pes':
    'share_biofuel_in_pes',
    'share e industry own use vs tfec in x2015':
    'share_e_industry_own_use_vs_tfec_in_x2015',
    'feist system':
    'feist_system',
    'aux1 1 1':
    'aux1_1_1',
    'efficiency rate of substitution':
    'efficiency_rate_of_substitution',
    'year policy to improve efficiency':
    'year_policy_to_improve_efficiency',
    'total fed households':
    'total_fed_households',
    'year policy change energy':
    'year_policy_change_energy',
    'policy change energy speed':
    'policy_change_energy_speed',
    'inertial rate energy intensity top down':
    'inertial_rate_energy_intensity_top_down',
    'final energy intensity 2020':
    'final_energy_intensity_2020',
    'variation energy intensity target':
    'variation_energy_intensity_target',
    'scarcity primary sources':
    'scarcity_primary_sources',
    'increase in perception ps scarcity':
    'increase_in_perception_ps_scarcity',
    'abundance primary sources':
    'abundance_primary_sources',
    'perception in primary sources scarcity':
    'perception_in_primary_sources_scarcity',
    'reduction in perception ps scarcity':
    'reduction_in_perception_ps_scarcity',
    'perception of inter fuel primary sources scarcity':
    'perception_of_inter_fuel_primary_sources_scarcity',
    'perception of inter fuel ps scarcity coal gas':
    'perception_of_inter_fuel_ps_scarcity_coal_gas',
    'perception of inter fuel ps scarcity coal oil':
    'perception_of_inter_fuel_ps_scarcity_coal_oil',
    'increase in perception fe scarcity h':
    'increase_in_perception_fe_scarcity_h',
    'perception of inter fuel ps scarcity gas coal':
    'perception_of_inter_fuel_ps_scarcity_gas_coal',
    'perception of inter fuel ps scarcity natx gas oil':
    'perception_of_inter_fuel_ps_scarcity_natx_gas_oil',
    'perception of inter fuel ps scarcity oil coal':
    'perception_of_inter_fuel_ps_scarcity_oil_coal',
    'sensitivity to energy scarcity medium':
    'sensitivity_to_energy_scarcity_medium',
    'perception of inter fuel ps scarcity oil natxgas':
    'perception_of_inter_fuel_ps_scarcity_oil_natxgas',
    'reduction in perception fe scarcity':
    'reduction_in_perception_fe_scarcity',
    'reduction in perception fe scarcity h':
    'reduction_in_perception_fe_scarcity_h',
    'sensitivity to scarcity option h':
    'sensitivity_to_scarcity_option_h',
    'energy scarcity forgetting time h':
    'energy_scarcity_forgetting_time_h',
    'increase in perception fe scarcity':
    'increase_in_perception_fe_scarcity',
    'sensitivity to energy scarcity high':
    'sensitivity_to_energy_scarcity_high',
    'perception of final energy scarcity':
    'perception_of_final_energy_scarcity',
    'perception of final energy scarcity h':
    'perception_of_final_energy_scarcity_h',
    'perception of inter fuel final energy scarcities h':
    'perception_of_inter_fuel_final_energy_scarcities_h',
    'perception of inter fuel final energy scarcities':
    'perception_of_inter_fuel_final_energy_scarcities',
    'scarcity final fuels h':
    'scarcity_final_fuels_h',
    'sensitivity to scarcity h':
    'sensitivity_to_scarcity_h',
    'sensitivity to scarcity':
    'sensitivity_to_scarcity',
    'scarcity final fuels':
    'scarcity_final_fuels',
    'sensitivity to energy scarcity low':
    'sensitivity_to_energy_scarcity_low',
    'sensitivity to scarcity option':
    'sensitivity_to_scarcity_option',
    'energy scarcity forgetting time':
    'energy_scarcity_forgetting_time',
    'year to finish policy change energy':
    'year_to_finish_policy_change_energy',
    'policy change energy speed sector uniform':
    'policy_change_energy_speed_sector_uniform',
    'pressure to improve energy intensity efficiency':
    'pressure_to_improve_energy_intensity_efficiency',
    'minimum fraction':
    'minimum_fraction',
    'choose final sectoral energy intensities evolution method':
    'choose_final_sectoral_energy_intensities_evolution_method',
    'decrease of intensity due to energy a technology change top down':
    'decrease_of_intensity_due_to_energy_a_technology_change_top_down',
    'policy to improve efficiency speed by sector':
    'policy_to_improve_efficiency_speed_by_sector',
    'rate change intensity bottom up':
    'rate_change_intensity_bottom_up',
    'inter fuel scarcity pressure':
    'inter_fuel_scarcity_pressure',
    'increase of intensity due to energy a technology change top down':
    'increase_of_intensity_due_to_energy_a_technology_change_top_down',
    'increase of intensity due to energy a technology eff':
    'increase_of_intensity_due_to_energy_a_technology_eff',
    'increase of intensity due to energy a technology net':
    'increase_of_intensity_due_to_energy_a_technology_net',
    'efficiency rate of substitution by sector':
    'efficiency_rate_of_substitution_by_sector',
    'share tech change fuel':
    'share_tech_change_fuel',
    'evol final energy intensity by sector and fuel':
    'evol_final_energy_intensity_by_sector_and_fuel',
    'fuel scarcity pressure':
    'fuel_scarcity_pressure',
    'fuel scarcity pressure h':
    'fuel_scarcity_pressure_h',
    'year policy to improve efficiency sector uniform':
    'year_policy_to_improve_efficiency_sector_uniform',
    'exp rapid evolution improve efficiency':
    'exp_rapid_evolution_improve_efficiency',
    'inter fuel scarcity pressure h':
    'inter_fuel_scarcity_pressure_h',
    'historical mean rate energy intensity':
    'historical_mean_rate_energy_intensity',
    'exp slow evolution improve efficiency':
    'exp_slow_evolution_improve_efficiency',
    'implementatio policy to change final energy':
    'implementatio_policy_to_change_final_energy',
    'policy to improve efficiency speed sector uniform':
    'policy_to_improve_efficiency_speed_sector_uniform',
    'final year target':
    'final_year_target',
    'activate bottom up method':
    'activate_bottom_up_method',
    'year change pct energy intensity target':
    'year_change_pct_energy_intensity_target',
    'year policy to improve efficiency by sector':
    'year_policy_to_improve_efficiency_by_sector',
    'aux20':
    'aux20',
    'year policy change energy by sector':
    'year_policy_change_energy_by_sector',
    'year policy change energy sector uniform':
    'year_policy_change_energy_sector_uniform',
    'energy intensity target by sector and fuel':
    'energy_intensity_target_by_sector_and_fuel',
    'maximum yearly acceleration of intensity improvement pct':
    'maximum_yearly_acceleration_of_intensity_improvement_pct',
    'available improvement efficiency':
    'available_improvement_efficiency',
    'initial global energy intensity by sector 2009':
    'initial_global_energy_intensity_by_sector_2009',
    'efficiency energy acceleration':
    'efficiency_energy_acceleration',
    'global energy intensity by sector':
    'global_energy_intensity_by_sector',
    'initial energy intensity by fuel and sector 1995':
    'initial_energy_intensity_by_fuel_and_sector_1995',
    'pressure to change energy technology by fuel':
    'pressure_to_change_energy_technology_by_fuel',
    'implementation policy to improve energy intensity efficiency':
    'implementation_policy_to_improve_energy_intensity_efficiency',
    'exp slow evol change energy':
    'exp_slow_evol_change_energy',
    'pressure to change energy technology':
    'pressure_to_change_energy_technology',
    'min energy intensity vs intial':
    'min_energy_intensity_vs_intial',
    'policy change energy speed by sector':
    'policy_change_energy_speed_by_sector',
    'year to finish energy intensity policies':
    'year_to_finish_energy_intensity_policies',
    'max yearly change':
    'max_yearly_change',
    'exp rapid evol change energy':
    'exp_rapid_evol_change_energy',
    'efficiency rate of substitution sector uniform':
    'efficiency_rate_of_substitution_sector_uniform',
    'inertial rate energy intensity h top down':
    'inertial_rate_energy_intensity_h_top_down',
    'final energy intensity by sector and fuel':
    'final_energy_intensity_by_sector_and_fuel',
    'implementation policy to improve energy intensity efficiency h':
    'implementation_policy_to_improve_energy_intensity_efficiency_h',
    'year to finish energy intensity policies h':
    'year_to_finish_energy_intensity_policies_h',
    'global energy intensity h':
    'global_energy_intensity_h',
    'pressure to improve energy intensity efficiency h':
    'pressure_to_improve_energy_intensity_efficiency_h',
    'minimum fraction h':
    'minimum_fraction_h',
    'policy change energy speed h sector uniform':
    'policy_change_energy_speed_h_sector_uniform',
    'policy to improve efficiency speed h':
    'policy_to_improve_efficiency_speed_h',
    'policy to improve efficiency speed h by sector':
    'policy_to_improve_efficiency_speed_h_by_sector',
    'policy to improve efficiency speed h sector uniform':
    'policy_to_improve_efficiency_speed_h_sector_uniform',
    'increase of intensity due to change energy technology eff h':
    'increase_of_intensity_due_to_change_energy_technology_eff_h',
    'increase of intensity due to change energy technology h top down':
    'increase_of_intensity_due_to_change_energy_technology_h_top_down',
    'increase of intensity due to change energy technology net h':
    'increase_of_intensity_due_to_change_energy_technology_net_h',
    'efficiency rate of substitution h sector uniform':
    'efficiency_rate_of_substitution_h_sector_uniform',
    'energy intensity target h':
    'energy_intensity_target_h',
    'evol final energy intensity h':
    'evol_final_energy_intensity_h',
    'activate scarcity feedback final fuel replacement quest':
    'activate_scarcity_feedback_final_fuel_replacement_quest',
    'activate transport h bottom up method':
    'activate_transport_h_bottom_up_method',
    'initial energy intensity 1995 h':
    'initial_energy_intensity_1995_h',
    'change total intensity to rest':
    'change_total_intensity_to_rest',
    'variation energy intensity target h':
    'variation_energy_intensity_target_h',
    'exp rapid evolution improve efficiency h':
    'exp_rapid_evolution_improve_efficiency_h',
    'initial global energy intensity 2009 h':
    'initial_global_energy_intensity_2009_h',
    'exp slow evolution change energy h':
    'exp_slow_evolution_change_energy_h',
    'final energy intensity 2020 h':
    'final_energy_intensity_2020_h',
    'exp slow evolution improve efficiency h':
    'exp_slow_evolution_improve_efficiency_h',
    'percentage of change over the historic maximun variation of energy intensities':
    'percentage_of_change_over_the_historic_maximun_variation_of_energy_intensities',
    'efficiency energy acceleration h':
    'efficiency_energy_acceleration_h',
    'final year target h':
    'final_year_target_h',
    'year policy change energy h':
    'year_policy_change_energy_h',
    'decrease of intensity due to change energy technology h top down':
    'decrease_of_intensity_due_to_change_energy_technology_h_top_down',
    'historical mean rate energy intensity h':
    'historical_mean_rate_energy_intensity_h',
    'aux19':
    'aux19',
    'year policy to improve efficiency h':
    'year_policy_to_improve_efficiency_h',
    'exp rapid evolution change energy h':
    'exp_rapid_evolution_change_energy_h',
    'max yearly change h':
    'max_yearly_change_h',
    'pressure to change energy technology h':
    'pressure_to_change_energy_technology_h',
    'energy intensity of households':
    'energy_intensity_of_households',
    'energy intensity of households rest':
    'energy_intensity_of_households_rest',
    'efficiency rate of substitution h by sector':
    'efficiency_rate_of_substitution_h_by_sector',
    'available improvement efficiency h':
    'available_improvement_efficiency_h',
    'policy change energy speed h by sector':
    'policy_change_energy_speed_h_by_sector',
    'year policy to improve efficiency h by sector':
    'year_policy_to_improve_efficiency_h_by_sector',
    'pressure to change energy technology by fuel h':
    'pressure_to_change_energy_technology_by_fuel_h',
    'year policy to improve efficiency h sector uniform':
    'year_policy_to_improve_efficiency_h_sector_uniform',
    'min energy intensity vs intial h':
    'min_energy_intensity_vs_intial_h',
    'year policy change energy h by sector':
    'year_policy_change_energy_h_by_sector',
    'year policy change energy h sector uniform':
    'year_policy_change_energy_h_sector_uniform',
    'pct change energy intensity target':
    'pct_change_energy_intensity_target',
    'share tech change fuel h':
    'share_tech_change_fuel_h',
    'choose policies of intensities global or by sector':
    'choose_policies_of_intensities_global_or_by_sector',
    'choose energy intensity target method':
    'choose_energy_intensity_target_method',
    'implementatio policy to change final energy h':
    'implementatio_policy_to_change_final_energy_h',
    'maximum yearly acceleration of intensity improvement pct h':
    'maximum_yearly_acceleration_of_intensity_improvement_pct_h',
    'policy change energy speed h':
    'policy_change_energy_speed_h',
    'efficiency rate of substitution h':
    'efficiency_rate_of_substitution_h',
    'households final energy demand':
    'households_final_energy_demand',
    'perception of inter fuel ps scarcity oil ff':
    'perception_of_inter_fuel_ps_scarcity_oil_ff',
    'max auxiliar elec':
    'max_auxiliar_elec',
    'increase share gas for elec':
    'increase_share_gas_for_elec',
    'decrease share gas for elec':
    'decrease_share_gas_for_elec',
    'decrease share oil for elec':
    'decrease_share_oil_for_elec',
    'future share gas plus coal div ff for elec':
    'future_share_gas_plus_coal_div_ff_for_elec',
    'future share gas div xcoal plus gasx for elec':
    'future_share_gas_div_xcoal_plus_gasx_for_elec',
    'future share oil div ff for elec':
    'future_share_oil_div_ff_for_elec',
    'perception of inter fuel ps scarcity ff oil':
    'perception_of_inter_fuel_ps_scarcity_ff_oil',
    'switch scarcity ps elec substit':
    'switch_scarcity_ps_elec_substit',
    'share gas div xcoal plus gasx for elec in x2014':
    'share_gas_div_xcoal_plus_gasx_for_elec_in_x2014',
    'increase share oil for elec':
    'increase_share_oil_for_elec',
    'share oil div ff for elec in x2015':
    'share_oil_div_ff_for_elec_in_x2015',
    'total fed trasnport households':
    'total_fed_trasnport_households',
    'transport households final energy demand':
    'transport_households_final_energy_demand',
    'modern bioe in households':
    'modern_bioe_in_households',
    'households total final energy demand':
    'households_total_final_energy_demand',
    'pe traditional biomass demand ej':
    'pe_traditional_biomass_demand_ej',
    'required fed by fuel before heat correction':
    'required_fed_by_fuel_before_heat_correction',
    'total transport fed by fuel':
    'total_transport_fed_by_fuel',
    'phs overcapacity':
    'phs_overcapacity',
    'potential fe elec stored phs twh':
    'potential_fe_elec_stored_phs_twh',
    'activate eroi quest':
    'activate_eroi_quest',
    'eroi fc system from 2015':
    'eroi_fc_system_from_2015',
    'ratio land productivity 2gen vs marg':
    'ratio_land_productivity_2gen_vs_marg',
    'land productivity biofuels marg ej mha':
    'land_productivity_biofuels_marg_ej_mha',
    'correction factor all ghgs':
    'correction_factor_all_ghgs',
    'cumulative co2e ghg emissions':
    'cumulative_co2e_ghg_emissions',
    'total ce all ghg':
    'total_ce_all_ghg',
    'total co2e all ghg':
    'total_co2e_all_ghg',
    'share in target year oil for heat':
    'share_in_target_year_oil_for_heat',
    'p share oil for heat':
    'p_share_oil_for_heat',
    'target year policy phase out oil for heat':
    'target_year_policy_phase_out_oil_for_heat',
    'b lineal regr phase out oil for heat':
    'b_lineal_regr_phase_out_oil_for_heat',
    'start year policy phase out oil for heat':
    'start_year_policy_phase_out_oil_for_heat',
    'start year policy phase out oil for elec':
    'start_year_policy_phase_out_oil_for_elec',
    'p share oil for elec':
    'p_share_oil_for_elec',
    'share in target year oil for elec':
    'share_in_target_year_oil_for_elec',
    'target year policy phase out oil for elec':
    'target_year_policy_phase_out_oil_for_elec',
    'b lineal regr phase out oil for elec':
    'b_lineal_regr_phase_out_oil_for_elec',
    'fed heat nc ej':
    'fed_heat_nc_ej',
    'leontief matrix':
    'leontief_matrix',
    'ia matrix':
    'ia_matrix',
    'pe traditional biomass consum ej':
    'pe_traditional_biomass_consum_ej',
    'scarcity resources counter':
    'scarcity_resources_counter',
    'scarcity resources flag':
    'scarcity_resources_flag',
    'percent res vs tpes':
    'percent_res_vs_tpes',
    'year init scarcity final fuels':
    'year_init_scarcity_final_fuels',
    'year init scarcity reserves':
    'year_init_scarcity_reserves',
    'percent tot monet invest reselec vs gdp':
    'percent_tot_monet_invest_reselec_vs_gdp',
    'scarcity final fuels counter':
    'scarcity_final_fuels_counter',
    'percent e losses cc':
    'percent_e_losses_cc',
    'scarcity reserves counter':
    'scarcity_reserves_counter',
    'year final scarcity reserves':
    'year_final_scarcity_reserves',
    'year final scarcity resources':
    'year_final_scarcity_resources',
    'scarcity fuels flag':
    'scarcity_fuels_flag',
    'scarcity reserves flag':
    'scarcity_reserves_flag',
    'year init scarcity resources':
    'year_init_scarcity_resources',
    'percent remaining potential tot res heat':
    'percent_remaining_potential_tot_res_heat',
    'abundance final fuels':
    'abundance_final_fuels',
    'scarcity final fuels flags':
    'scarcity_final_fuels_flags',
    'percent remaining potential tot res elec':
    'percent_remaining_potential_tot_res_elec',
    'year final scarcity final fuels':
    'year_final_scarcity_final_fuels',
    'share blue water use vs ar':
    'share_blue_water_use_vs_ar',
    'ar water':
    'ar_water',
    'share total water use vs ar':
    'share_total_water_use_vs_ar',
    'renewable water resources':
    'renewable_water_resources',
    'share blue water use vs renewable water resources':
    'share_blue_water_use_vs_renewable_water_resources',
    'dam3 per km3':
    'dam3_per_km3',
    'share total water use vs renewable water resources':
    'share_total_water_use_vs_renewable_water_resources',
    'total pe solid bioe potential heat plus elec ej':
    'total_pe_solid_bioe_potential_heat_plus_elec_ej',
    'land module activated quest':
    'land_module_activated_quest',
    'cp res for heat':
    'cp_res_for_heat',
    'potential fes res for heat com ej':
    'potential_fes_res_for_heat_com_ej',
    'potential fes res for heat com twh':
    'potential_fes_res_for_heat_com_twh',
    'real generation res elec twh':
    'real_generation_res_elec_twh',
    'potential fes res for heat nc twh':
    'potential_fes_res_for_heat_nc_twh',
    'replacement capacity res elec':
    'replacement_capacity_res_elec',
    'cp res elec':
    'cp_res_elec',
    'replacement res for heat nc tw':
    'replacement_res_for_heat_nc_tw',
    'replacement res for heat com tw':
    'replacement_res_for_heat_com_tw',
    'max eroi fc':
    'max_eroi_fc',
    'eroi fc system from 2015 1':
    'eroi_fc_system_from_2015_1',
    'p rr ti rest':
    'p_rr_ti_rest',
    'p rr li rest':
    'p_rr_li_rest',
    'p rr v rest':
    'p_rr_v_rest',
    'p rr mg rest':
    'p_rr_mg_rest',
    'p rr zn rest':
    'p_rr_zn_rest',
    'p rr minerals rest':
    'p_rr_minerals_rest',
    'p rr cd rest':
    'p_rr_cd_rest',
    'improvement recycling rates minerals rest':
    'improvement_recycling_rates_minerals_rest',
    'b lineal regr rr alt techn':
    'b_lineal_regr_rr_alt_techn',
    'b lineal regr rr rest':
    'b_lineal_regr_rr_rest',
    'by mineral rr rest 1yr':
    'by_mineral_rr_rest_1yr',
    'p rr cu rest':
    'p_rr_cu_rest',
    'a lineal regr rr alt techn':
    'a_lineal_regr_rr_alt_techn',
    'a lineal regr rr rest':
    'a_lineal_regr_rr_rest',
    'start year p rr minerals rest':
    'start_year_p_rr_minerals_rest',
    'common rr minerals variation rest':
    'common_rr_minerals_variation_rest',
    'p rr in rest':
    'p_rr_in_rest',
    'p rr te rest':
    'p_rr_te_rest',
    'p rr mo rest':
    'p_rr_mo_rest',
    'by mineral rr rest':
    'by_mineral_rr_rest',
    'p rr ag rest':
    'p_rr_ag_rest',
    'p rr mn rest':
    'p_rr_mn_rest',
    'p rr al rest':
    'p_rr_al_rest',
    'target year p rr minerals rest':
    'target_year_p_rr_minerals_rest',
    'p rr ga rest':
    'p_rr_ga_rest',
    'p rr sn rest':
    'p_rr_sn_rest',
    'p rr pb rest':
    'p_rr_pb_rest',
    'p rr cr rest':
    'p_rr_cr_rest',
    'p rr ni rest':
    'p_rr_ni_rest',
    'p rr fe rest':
    'p_rr_fe_rest',
    'by mineral rr variation rest':
    'by_mineral_rr_variation_rest',
    'current recycling rates minerals alt techn':
    'current_recycling_rates_minerals_alt_techn',
    'p rr mg alt techn':
    'p_rr_mg_alt_techn',
    'p rr minerals alt techn':
    'p_rr_minerals_alt_techn',
    'p rr mn alt techn':
    'p_rr_mn_alt_techn',
    'p rr mo alt techn':
    'p_rr_mo_alt_techn',
    'p rr ni alt techn':
    'p_rr_ni_alt_techn',
    'p rr pb alt techn':
    'p_rr_pb_alt_techn',
    'by mineral rr alt techn':
    'by_mineral_rr_alt_techn',
    'by mineral rr alt techn 1yr':
    'by_mineral_rr_alt_techn_1yr',
    'p rr al alt techn':
    'p_rr_al_alt_techn',
    'p rr cd alt techn':
    'p_rr_cd_alt_techn',
    'p rr cu alt techn':
    'p_rr_cu_alt_techn',
    'p rr fe alt techn':
    'p_rr_fe_alt_techn',
    'p rr ga alt techn':
    'p_rr_ga_alt_techn',
    'p rr in alt techn':
    'p_rr_in_alt_techn',
    'p rr li alt techn':
    'p_rr_li_alt_techn',
    'recycling rates minerals alt techn':
    'recycling_rates_minerals_alt_techn',
    'p rr v alt techn':
    'p_rr_v_alt_techn',
    'p rr zn alt techn':
    'p_rr_zn_alt_techn',
    'p rr ti alt techn':
    'p_rr_ti_alt_techn',
    'p rr cr alt techn':
    'p_rr_cr_alt_techn',
    'p rr ag alt techn':
    'p_rr_ag_alt_techn',
    'p rr sn alt techn':
    'p_rr_sn_alt_techn',
    'p rr te alt techn':
    'p_rr_te_alt_techn',
    'improvement recycling rates minerals alt techn':
    'improvement_recycling_rates_minerals_alt_techn',
    'by mineral rr variation alt techn':
    'by_mineral_rr_variation_alt_techn',
    'start year p rr minerals alt techn':
    'start_year_p_rr_minerals_alt_techn',
    'target year p rr minerals alt techn':
    'target_year_p_rr_minerals_alt_techn',
    'temp change 15c':
    'temp_change_15c',
    'density':
    'density',
    'sec per day':
    'sec_per_day',
    'sec per yr':
    'sec_per_yr',
    'init atmos uocean temp':
    'init_atmos_uocean_temp',
    'watt per j s':
    'watt_per_j_s',
    'lower layer volume vu':
    'lower_layer_volume_vu',
    'volumetric heat capacity':
    'volumetric_heat_capacity',
    'mass heat cap':
    'mass_heat_cap',
    'heat diffusion covar':
    'heat_diffusion_covar',
    'twox co2x forcing':
    'twox_co2x_forcing',
    'climate sensitivity to 2x co2':
    'climate_sensitivity_to_2x_co2',
    'temperature change':
    'temperature_change',
    'land thickness':
    'land_thickness',
    'heat transfer':
    'heat_transfer',
    'climate feedback param':
    'climate_feedback_param',
    'area':
    'area',
    'heat transfer coeff':
    'heat_transfer_coeff',
    'eddy diff coeff':
    'eddy_diff_coeff',
    'upper layer volume vu':
    'upper_layer_volume_vu',
    'heat in deep ocean':
    'heat_in_deep_ocean',
    'land area fraction':
    'land_area_fraction',
    'relative deep ocean temp':
    'relative_deep_ocean_temp',
    'co2 rad force coeffcroads':
    'co2_rad_force_coeffcroads',
    'temp change 2':
    'temp_change_2',
    'feedback cooling':
    'feedback_cooling',
    'heat transfer rate':
    'heat_transfer_rate',
    'atm and upper ocean heat cap':
    'atm_and_upper_ocean_heat_cap',
    'deep ocean heat cap':
    'deep_ocean_heat_cap',
    'init deep ocean temp':
    'init_deep_ocean_temp',
    'heat in atmosphere and upper ocean':
    'heat_in_atmosphere_and_upper_ocean',
    'ch4 n2o unit adj':
    'ch4_n2o_unit_adj',
    'adjustment for ch4ref and n2oref':
    'adjustment_for_ch4ref_and_n2oref',
    'ch4 radiative efficiency coefficient':
    'ch4_radiative_efficiency_coefficient',
    'total radiative forcing':
    'total_radiative_forcing',
    'last historical rf year':
    'last_historical_rf_year',
    'ch4 reference conc':
    'ch4_reference_conc',
    'rf from f gases':
    'rf_from_f_gases',
    'well mixed ghg forcing':
    'well_mixed_ghg_forcing',
    'mineral aerosols and land rf':
    'mineral_aerosols_and_land_rf',
    'time to commit rf':
    'time_to_commit_rf',
    'ch4 n20 inter exp':
    'ch4_n20_inter_exp',
    'ch4 n20 inter exp 2':
    'ch4_n20_inter_exp_2',
    'ch4 n2o inter coef 2':
    'ch4_n2o_inter_coef_2',
    'adjusted other forcings':
    'adjusted_other_forcings',
    'adjustment for ch4 and n2oref':
    'adjustment_for_ch4_and_n2oref',
    'adjustment for ch4ref and n2o':
    'adjustment_for_ch4ref_and_n2o',
    'n2o reference conc':
    'n2o_reference_conc',
    'delay effective radiative forcing':
    'delay_effective_radiative_forcing',
    'effective radiative forcing':
    'effective_radiative_forcing',
    'co2 rad force':
    'co2_rad_force',
    'co2 radiative forcing':
    'co2_radiative_forcing',
    'ch4 n2o interaction coeffient':
    'ch4_n2o_interaction_coeffient',
    'n2o radiative efficiency coefficient':
    'n2o_radiative_efficiency_coefficient',
    'ch4 n2o inter coef 3':
    'ch4_n2o_inter_coef_3',
    'n2o radiative forcing':
    'n2o_radiative_forcing',
    'ch4 radiative forcing':
    'ch4_radiative_forcing',
    'other ghg rad forcing xnon co2x':
    'other_ghg_rad_forcing_xnon_co2x',
    'ch4 and n2o radiative forcing':
    'ch4_and_n2o_radiative_forcing',
    'hfc rf total':
    'hfc_rf_total',
    'time const for hfc':
    'time_const_for_hfc',
    'time const for n2o':
    'time_const_for_n2o',
    'time const for pfc':
    'time_const_for_pfc',
    'sensitivity of methane emissions to permafrost and clathrate':
    'sensitivity_of_methane_emissions_to_permafrost_and_clathrate',
    'reference ch4 time constant':
    'reference_ch4_time_constant',
    'stratospheric ch4 path share':
    'stratospheric_ch4_path_share',
    'g per ton':
    'g_per_ton',
    'init pfc in atm con':
    'init_pfc_in_atm_con',
    'inital hfc con':
    'inital_hfc_con',
    'sf6':
    'sf6',
    'sf6 atm conc':
    'sf6_atm_conc',
    'sf6 molar mass':
    'sf6_molar_mass',
    'sf6 radiative efficiency':
    'sf6_radiative_efficiency',
    'sf6 rf':
    'sf6_rf',
    'sf6 uptake':
    'sf6_uptake',
    'initial ch4':
    'initial_ch4',
    'initial ch4 conc':
    'initial_ch4_conc',
    'pfc radiative efficiency':
    'pfc_radiative_efficiency',
    'ch4 emissions from permafrost and clathrate':
    'ch4_emissions_from_permafrost_and_clathrate',
    'hfc in atm':
    'hfc_in_atm',
    'hfc molar mass':
    'hfc_molar_mass',
    'hfc radiative efficiency':
    'hfc_radiative_efficiency',
    'ch4 fractional uptake':
    'ch4_fractional_uptake',
    'hfc uptake':
    'hfc_uptake',
    'total c from permafrost':
    'total_c_from_permafrost',
    'ch4 molar mass':
    'ch4_molar_mass',
    'n2o n molar mass':
    'n2o_n_molar_mass',
    'ch4 uptake':
    'ch4_uptake',
    'total ch4 released':
    'total_ch4_released',
    'natural pfc emissions':
    'natural_pfc_emissions',
    'choose rcp':
    'choose_rcp',
    'pfc atm conc':
    'pfc_atm_conc',
    'ppb ch4 per mton ch4':
    'ppb_ch4_per_mton_ch4',
    'ppb n2o per mtonn':
    'ppb_n2o_per_mtonn',
    'ppt hfc per tons hfc':
    'ppt_hfc_per_tons_hfc',
    'ppt per mol':
    'ppt_per_mol',
    'ppt per ppb':
    'ppt_per_ppb',
    'ppt pfc per tons pfc':
    'ppt_pfc_per_tons_pfc',
    'c from ch4 oxidation':
    'c_from_ch4_oxidation',
    'reference sensitivity of ch4 from permafrost and clathrate to temperature':
    'reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature',
    'global ch4 emissions':
    'global_ch4_emissions',
    'preindustrial ch4':
    'preindustrial_ch4',
    'preindustrial hfc conc':
    'preindustrial_hfc_conc',
    'pfc in atm':
    'pfc_in_atm',
    'initial sf6 con':
    'initial_sf6_con',
    'pfc rf':
    'pfc_rf',
    'pfc uptake':
    'pfc_uptake',
    'init pfc in atm':
    'init_pfc_in_atm',
    'n2o atm conc':
    'n2o_atm_conc',
    'n2o in atm':
    'n2o_in_atm',
    'n2o uptake':
    'n2o_uptake',
    'hfc atm conc':
    'hfc_atm_conc',
    'ton per mton':
    'ton_per_mton',
    'natural n2o emissions':
    'natural_n2o_emissions',
    'cf4 molar mass':
    'cf4_molar_mass',
    'ch4 atm conc':
    'ch4_atm_conc',
    'preindustrial sf6 conc':
    'preindustrial_sf6_conc',
    'time const for ch4':
    'time_const_for_ch4',
    'initial hfc':
    'initial_hfc',
    'flux c from permafrost release':
    'flux_c_from_permafrost_release',
    'global n2o emissions':
    'global_n2o_emissions',
    'tropospheric ch4 path share':
    'tropospheric_ch4_path_share',
    'preindustrial pfc':
    'preindustrial_pfc',
    'ppt sf6 per tons sf6':
    'ppt_sf6_per_tons_sf6',
    'hfc rf':
    'hfc_rf',
    'initial n2o':
    'initial_n2o',
    'initial n2o conc':
    'initial_n2o_conc',
    'temperature threshold for methane emissions from permafrost and clathrate':
    'temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate',
    'time const for sf6':
    'time_const_for_sf6',
    'preindustrial pfc conc':
    'preindustrial_pfc_conc',
    'initial sf6':
    'initial_sf6',
    'reference sensitivity of c from permafrost and clathrate to temperature':
    'reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature',
    'global total pfc emissions':
    'global_total_pfc_emissions',
    'ch4 in atm':
    'ch4_in_atm',
    'global anthropogenic ch4 emissions':
    'global_anthropogenic_ch4_emissions',
    'sensitivity of pco2 dic to temperature':
    'sensitivity_of_pco2_dic_to_temperature',
    'sensitivity of pco2 dic to temperature mean':
    'sensitivity_of_pco2_dic_to_temperature_mean',
    'mean depth of adjacent layers':
    'mean_depth_of_adjacent_layers',
    'diffusion flux':
    'diffusion_flux',
    'init c in biomass':
    'init_c_in_biomass',
    'init c in deep ocean per meter':
    'init_c_in_deep_ocean_per_meter',
    'init c in humus':
    'init_c_in_humus',
    'flux atm to biomass':
    'flux_atm_to_biomass',
    'flux atm to ocean':
    'flux_atm_to_ocean',
    'flux biomass to atmosphere':
    'flux_biomass_to_atmosphere',
    'flux biomass to ch4':
    'flux_biomass_to_ch4',
    'flux biomass to humus':
    'flux_biomass_to_humus',
    'flux biosphere to ch4':
    'flux_biosphere_to_ch4',
    'flux humus to atmosphere':
    'flux_humus_to_atmosphere',
    'co2 ppm concentrations':
    'co2_ppm_concentrations',
    'total c anthro emissions':
    'total_c_anthro_emissions',
    'effect of temp on dic pco2':
    'effect_of_temp_on_dic_pco2',
    'effect of warming on c flux to biomass':
    'effect_of_warming_on_c_flux_to_biomass',
    'effect of warming on ch4 release from biological activity':
    'effect_of_warming_on_ch4_release_from_biological_activity',
    'c in mixed layer per meter':
    'c_in_mixed_layer_per_meter',
    'biomass res time':
    'biomass_res_time',
    'biostim coeff':
    'biostim_coeff',
    'mtons per gtons':
    'mtons_per_gtons',
    'biostim coeff mean':
    'biostim_coeff_mean',
    'buff c coeff':
    'buff_c_coeff',
    'natural ch4 emissions':
    'natural_ch4_emissions',
    'humification fraction':
    'humification_fraction',
    'humus res time':
    'humus_res_time',
    'layer depth':
    'layer_depth',
    'ref buffer factor':
    'ref_buffer_factor',
    'reference temperature change for effect of warming on ch4 from respiration':
    'reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration',
    'c in humus':
    'c_in_humus',
    'c in mixed layer':
    'c_in_mixed_layer',
    'init c in atmos':
    'init_c_in_atmos',
    'strength of temp effect on land c flux mean':
    'strength_of_temp_effect_on_land_c_flux_mean',
    'pre industrial value ppm':
    'pre_industrial_value_ppm',
    'biostim coeff index':
    'biostim_coeff_index',
    'init c in mixed ocean per meter':
    'init_c_in_mixed_ocean_per_meter',
    'init co2 in atmos ppm':
    'init_co2_in_atmos_ppm',
    'init npp':
    'init_npp',
    'buffer factor':
    'buffer_factor',
    'c in atmosphere':
    'c_in_atmosphere',
    'mixed depth':
    'mixed_depth',
    'mixing time':
    'mixing_time',
    'c in deep ocean per meter':
    'c_in_deep_ocean_per_meter',
    'elf concentrations logistic':
    'elf_concentrations_logistic',
    'strength of temp effect on c flux to land':
    'strength_of_temp_effect_on_c_flux_to_land',
    'ch4 generation rate from humus':
    'ch4_generation_rate_from_humus',
    'preind c in mixed layer':
    'preind_c_in_mixed_layer',
    'preind ocean c per meter':
    'preind_ocean_c_per_meter',
    'preindustrial c':
    'preindustrial_c',
    'equilibrium c per meter in mixed layer':
    'equilibrium_c_per_meter_in_mixed_layer',
    'sensitivity of c uptake to temperature':
    'sensitivity_of_c_uptake_to_temperature',
    'ch4 generation rate from biomass':
    'ch4_generation_rate_from_biomass',
    'ch4 per c':
    'ch4_per_c',
    'flux humus to ch4':
    'flux_humus_to_ch4',
    'sensitivity of methane emissions to temperature':
    'sensitivity_of_methane_emissions_to_temperature',
    'eddy diff coeff index':
    'eddy_diff_coeff_index',
    'c in biomass':
    'c_in_biomass',
    'gtc per ppm':
    'gtc_per_ppm',
    'c in deep ocean':
    'c_in_deep_ocean',
    'equil c in mixed layer':
    'equil_c_in_mixed_layer',
    'layer time constant':
    'layer_time_constant',
    'eddy diff mean':
    'eddy_diff_mean',
    'common rr minerals variation alt techn':
    'common_rr_minerals_variation_alt_techn',
    'choose targets mineral recycling rates':
    'choose_targets_mineral_recycling_rates',
    'total water use per capita':
    'total_water_use_per_capita',
    'total water use':
    'total_water_use',
    'water use per type per capita':
    'water_use_per_type_per_capita',
    'variation water intensity by sector':
    'variation_water_intensity_by_sector',
    'historic water intensities by sector delayed 1yr':
    'historic_water_intensities_by_sector_delayed_1yr',
    'historic water intensities for households delayed 1yr':
    'historic_water_intensities_for_households_delayed_1yr',
    'variation water intensity households':
    'variation_water_intensity_households',
    'water intensity for households':
    'water_intensity_for_households',
    'total water use by type':
    'total_water_use_by_type',
    'total water for o and m required by res elec dam3':
    'total_water_for_o_and_m_required_by_res_elec_dam3',
    'initial water intensity for households':
    'initial_water_intensity_for_households',
    'water intensity by sector':
    'water_intensity_by_sector',
    'water use by sector':
    'water_use_by_sector',
    'water use by households':
    'water_use_by_households',
    'tfec res ej':
    'tfec_res_ej',
    'pe traditional biomass ej delayed 1yr':
    'pe_traditional_biomass_ej_delayed_1yr',
    'population dependent on trad biomass':
    'population_dependent_on_trad_biomass',
    'mt to dam3':
    'mt_to_dam3',
    'total water for o and m required by res elec':
    'total_water_for_o_and_m_required_by_res_elec',
    'initial water intensity by sector':
    'initial_water_intensity_by_sector',
    'initial water use by households':
    'initial_water_use_by_households',
    'initial water use by sector':
    'initial_water_use_by_sector',
    'max potential npp bioe conventional for heat plus elec':
    'max_potential_npp_bioe_conventional_for_heat_plus_elec',
    'diff demand':
    'diff_demand',
    'variation lc':
    'variation_lc',
    'variation cc':
    'variation_cc',
    'demand by sector fd adjusted':
    'demand_by_sector_fd_adjusted',
    'total demand adjusted':
    'total_demand_adjusted',
    'desired gdp':
    'desired_gdp',
    'demand by sector':
    'demand_by_sector',
    'aux4':
    'aux4',
    'one year':
    'one_year',
    'eptb dynamic':
    'eptb_dynamic',
    'eroist system delayed':
    'eroist_system_delayed',
    'eroist system delayed 1yr':
    'eroist_system_delayed_1yr',
    'pipeline transport constant 26x ej in x2014':
    'pipeline_transport_constant_26x_ej_in_x2014',
    'total distribution losses':
    'total_distribution_losses',
    'ia matrix 2002':
    'ia_matrix_2002',
    'ia matrix 2003':
    'ia_matrix_2003',
    'ia matrix 2004':
    'ia_matrix_2004',
    'ia matrix 2005':
    'ia_matrix_2005',
    'ia matrix 2006':
    'ia_matrix_2006',
    'ia matrix 2007':
    'ia_matrix_2007',
    'ia matrix 2008':
    'ia_matrix_2008',
    'ia matrix for python':
    'ia_matrix_for_python',
    'ia matrix 1995':
    'ia_matrix_1995',
    'ia matrix 1996':
    'ia_matrix_1996',
    'ia matrix 1997':
    'ia_matrix_1997',
    'ia matrix 1998':
    'ia_matrix_1998',
    'ia matrix 1999':
    'ia_matrix_1999',
    'ia matrix 2000':
    'ia_matrix_2000',
    'ia matrix 2001':
    'ia_matrix_2001',
    'ia matrix 2009':
    'ia_matrix_2009',
    'leontief matrix for python':
    'leontief_matrix_for_python',
    'leontief matrix 1996':
    'leontief_matrix_1996',
    'leontief matrix 1997':
    'leontief_matrix_1997',
    'leontief matrix 1998':
    'leontief_matrix_1998',
    'leontief matrix 1999':
    'leontief_matrix_1999',
    'leontief matrix 2000':
    'leontief_matrix_2000',
    'leontief matrix 2001':
    'leontief_matrix_2001',
    'leontief matrix 2002':
    'leontief_matrix_2002',
    'leontief matrix 2003':
    'leontief_matrix_2003',
    'leontief matrix 2004':
    'leontief_matrix_2004',
    'leontief matrix 2005':
    'leontief_matrix_2005',
    'leontief matrix 2006':
    'leontief_matrix_2006',
    'leontief matrix 2007':
    'leontief_matrix_2007',
    'leontief matrix 2008':
    'leontief_matrix_2008',
    'leontief matrix 2009':
    'leontief_matrix_2009',
    'leontief matrix 1995':
    'leontief_matrix_1995',
    'replacement batteries':
    'replacement_batteries',
    'share of electric light vehicles':
    'share_of_electric_light_vehicles',
    'share elec plus hyb light vehicles':
    'share_elec_plus_hyb_light_vehicles',
    'aux p inland transp':
    'aux_p_inland_transp',
    't fin inlandt':
    't_fin_inlandt',
    'h elec initial growth':
    'h_elec_initial_growth',
    't fin h veh':
    't_fin_h_veh',
    'h gas initial growth':
    'h_gas_initial_growth',
    't ini h veh':
    't_ini_h_veh',
    'h hyb initial growth':
    'h_hyb_initial_growth',
    'policy 2wheels':
    'policy_2wheels',
    'h 2w initial growth':
    'h_2w_initial_growth',
    'var percents h vehicles':
    'var_percents_h_vehicles',
    'increase households energy final demand for transp':
    'increase_households_energy_final_demand_for_transp',
    'start year p common rr minerals alt techn':
    'start_year_p_common_rr_minerals_alt_techn',
    'start year p common rr minerals rest':
    'start_year_p_common_rr_minerals_rest',
    'select pop ssps':
    'select_pop_ssps',
    'dynamic low range fec good standard of living':
    'dynamic_low_range_fec_good_standard_of_living',
    'cp ev batteries for elec storage':
    'cp_ev_batteries_for_elec_storage',
    'dynamic threshold xhigh developmentx':
    'dynamic_threshold_xhigh_developmentx',
    'max cp ev batteries for elec storage':
    'max_cp_ev_batteries_for_elec_storage',
    'tfec intensity until 2009':
    'tfec_intensity_until_2009',
    'desired annual gdp growth rate':
    'desired_annual_gdp_growth_rate',
    'cumulative tfec intensity change from 2009':
    'cumulative_tfec_intensity_change_from_2009',
    'lifetime ev batteries':
    'lifetime_ev_batteries',
    'dynamic high range fec good standard of living':
    'dynamic_high_range_fec_good_standard_of_living',
    'tfec per capita':
    'tfec_per_capita',
    'aux15':
    'aux15',
    'cp ev batteries for transp':
    'cp_ev_batteries_for_transp',
    'p customized cte gdppc variation':
    'p_customized_cte_gdppc_variation',
    'annual growth rate electricity generation res elec tot':
    'annual_growth_rate_electricity_generation_res_elec_tot',
    'annual growth rate res for heat':
    'annual_growth_rate_res_for_heat',
    'p customized year pop evolution':
    'p_customized_year_pop_evolution',
    'select gdppc evolution input':
    'select_gdppc_evolution_input',
    'select population evolution input':
    'select_population_evolution_input',
    'p customized year gdppc evolution':
    'p_customized_year_gdppc_evolution',
    'fe tot generation all res elec twh delayed 1yr':
    'fe_tot_generation_all_res_elec_twh_delayed_1yr',
    'p customized cte pop variation':
    'p_customized_cte_pop_variation',
    'fes res for heat delayed 1yr':
    'fes_res_for_heat_delayed_1yr',
    'desired gdp delayed 1yr':
    'desired_gdp_delayed_1yr',
    'diff annual gdp growth rate':
    'diff_annual_gdp_growth_rate',
    'gdppc initial year':
    'gdppc_initial_year',
    'desired gdppc':
    'desired_gdppc',
    'tpes intensity until 2009':
    'tpes_intensity_until_2009',
    'share e losses cc until x2015':
    'share_e_losses_cc_until_x2015',
    'aux13':
    'aux13',
    'aux14':
    'aux14',
    'share e losses cc from x2015':
    'share_e_losses_cc_from_x2015',
    'elf':
    'elf',
    'cumulative tpes intensity change from 2009':
    'cumulative_tpes_intensity_change_from_2009',
    'cumulative tfec intensity change from 2009 without eroi':
    'cumulative_tfec_intensity_change_from_2009_without_eroi',
    'tfec intensity until 2009 without eroi':
    'tfec_intensity_until_2009_without_eroi',
    'tfei sectors':
    'tfei_sectors',
    'annual tfes intensity growth rate without eroi':
    'annual_tfes_intensity_growth_rate_without_eroi',
    'tfes intensity without eroi delayed 1yr':
    'tfes_intensity_without_eroi_delayed_1yr',
    'required tfed sectors':
    'required_tfed_sectors',
    'ratio fed households vs sectors':
    'ratio_fed_households_vs_sectors',
    'tfes intensity ej tdollar without eroi':
    'tfes_intensity_ej_tdollar_without_eroi',
    'ghg emissions 2050 mlt2030':
    'ghg_emissions_2050_mlt2030',
    'ghg emissions 2050 mlt2020':
    'ghg_emissions_2050_mlt2020',
    'start year p growth res elec':
    'start_year_p_growth_res_elec',
    'start year p growth res heat':
    'start_year_p_growth_res_heat',
    'labour share growth':
    'labour_share_growth',
    'year initial labour share':
    'year_initial_labour_share',
    'year final labour share':
    'year_final_labour_share',
    'p labour share 2050':
    'p_labour_share_2050',
    'initial labour share':
    'initial_labour_share',
    'low range fec good standard of living':
    'low_range_fec_good_standard_of_living',
    'threshold fec xhigh developmentx':
    'threshold_fec_xhigh_developmentx',
    'high range fec good standard of living':
    'high_range_fec_good_standard_of_living',
    'total co2exgwp equal 100 yearsx':
    'total_co2exgwp_equal_100_yearsx',
    'net tfec per capita':
    'net_tfec_per_capita',
    'gwp 100 years ch4':
    'gwp_100_years_ch4',
    'activate energy scarcity feedback quest':
    'activate_energy_scarcity_feedback_quest',
    'max potential phs twh':
    'max_potential_phs_twh',
    'replacement rate phs':
    'replacement_rate_phs',
    'energy scarcity feedback shortage coeff':
    'energy_scarcity_feedback_shortage_coeff',
    'real fe elec stored ev batteries twh':
    'real_fe_elec_stored_ev_batteries_twh',
    'share tot fei res elec var':
    'share_tot_fei_res_elec_var',
    'cp ev batteries required':
    'cp_ev_batteries_required',
    'output ev bateries for storage over lifetime':
    'output_ev_bateries_for_storage_over_lifetime',
    'discarded batteries':
    'discarded_batteries',
    'esoi elec storage':
    'esoi_elec_storage',
    'esoi ev batteries':
    'esoi_ev_batteries',
    'rt elec storage efficiency':
    'rt_elec_storage_efficiency',
    'abundance storage':
    'abundance_storage',
    'used ev batteries for elec storage':
    'used_ev_batteries_for_elec_storage',
    'max cp ev batteries':
    'max_cp_ev_batteries',
    'total capacity elec storage tw':
    'total_capacity_elec_storage_tw',
    'demand ev batteries for elec storage':
    'demand_ev_batteries_for_elec_storage',
    'ced per tw over lifetime phs':
    'ced_per_tw_over_lifetime_phs',
    'remaining potential constraint on new phs capacity':
    'remaining_potential_constraint_on_new_phs_capacity',
    'new required phs capacity':
    'new_required_phs_capacity',
    'share dyn fei for res vs tfec':
    'share_dyn_fei_for_res_vs_tfec',
    'fei ev batteries':
    'fei_ev_batteries',
    'output phs over lifetime':
    'output_phs_over_lifetime',
    'esoi static phs':
    'esoi_static_phs',
    'total dyn fei res':
    'total_dyn_fei_res',
    'adapt growth res elec after allocation':
    'adapt_growth_res_elec_after_allocation',
    'esoi phs':
    'esoi_phs',
    'p phs growth':
    'p_phs_growth',
    'constraint elec storage availability':
    'constraint_elec_storage_availability',
    'eroist system':
    'eroist_system',
    'initial instal cap phs':
    'initial_instal_cap_phs',
    'cedtot over lifetime phs':
    'cedtot_over_lifetime_phs',
    'installed capacity phs tw':
    'installed_capacity_phs_tw',
    'phs capacity under construction':
    'phs_capacity_under_construction',
    'past phs capacity growth':
    'past_phs_capacity_growth',
    'new phs capacity under planning':
    'new_phs_capacity_under_planning',
    'wear phs':
    'wear_phs',
    'replacement capacity phs':
    'replacement_capacity_phs',
    'real fe elec stored phs twh':
    'real_fe_elec_stored_phs_twh',
    'phs planned capacity':
    'phs_planned_capacity',
    'final energy invested phs':
    'final_energy_invested_phs',
    'remaining potential phs':
    'remaining_potential_phs',
    'initial capacity in construction phs':
    'initial_capacity_in_construction_phs',
    'required capacity phs':
    'required_capacity_phs',
    'total fei over lifetime res elec dispatch':
    'total_fei_over_lifetime_res_elec_dispatch',
    'min lifetime ev batteries':
    'min_lifetime_ev_batteries',
    'total final energy invested res elec var':
    'total_final_energy_invested_res_elec_var',
    'materials required for ev batteries mt':
    'materials_required_for_ev_batteries_mt',
    'new plus replaced batteries tw':
    'new_plus_replaced_batteries_tw',
    'energy intensity construction ev batteries mj div mw':
    'energy_intensity_construction_ev_batteries_mj_div_mw',
    'new batteries':
    'new_batteries',
    'batteries ev plus hib plus x2we':
    'batteries_ev_plus_hib_plus_x2we',
    'kw per mw':
    'kw_per_mw',
    'net stored energy ev battery over lifetime':
    'net_stored_energy_ev_battery_over_lifetime',
    'grid correction factor ev batteries':
    'grid_correction_factor_ev_batteries',
    'share energy requirements for decom ev batteries':
    'share_energy_requirements_for_decom_ev_batteries',
    'working hours per year':
    'working_hours_per_year',
    'days per year':
    'days_per_year',
    'total energy required for material consumption for res elec':
    'total_energy_required_for_material_consumption_for_res_elec',
    'total energy required for material consumption per res elec':
    'total_energy_required_for_material_consumption_per_res_elec',
    'mw in 1 year to mj':
    'mw_in_1_year_to_mj',
    'working hours per day':
    'working_hours_per_day',
    'annual work hours for res':
    'annual_work_hours_for_res',
    'hours work per gj res delivered':
    'hours_work_per_gj_res_delivered',
    'total energy required for total material consumption for ev batteries':
    'total_energy_required_for_total_material_consumption_for_ev_batteries',
    'tfe required for total material consumption for alt techn':
    'tfe_required_for_total_material_consumption_for_alt_techn',
    'energy required for material consumption per res elec':
    'energy_required_for_material_consumption_per_res_elec',
    'total energy required per material for alt techn':
    'total_energy_required_per_material_for_alt_techn',
    'total jobs res elec':
    'total_jobs_res_elec',
    'total jobs biofuels':
    'total_jobs_biofuels',
    'total jobs res':
    'total_jobs_res',
    'total d plus i jobs res heat per techn':
    'total_d_plus_i_jobs_res_heat_per_techn',
    'total jobs res heat':
    'total_jobs_res_heat',
    'total d plus i jobs res elec per techn':
    'total_d_plus_i_jobs_res_elec_per_techn',
    'ratio total vs d jobs res heat':
    'ratio_total_vs_d_jobs_res_heat',
    'ratio total vs d jobs res elec':
    'ratio_total_vs_d_jobs_res_elec',
    'employment factor biofuels':
    'employment_factor_biofuels',
    'installed capacity res elec delayed 1yr':
    'installed_capacity_res_elec_delayed_1yr',
    'jobs o and m res heat per techn':
    'jobs_o_and_m_res_heat_per_techn',
    'd jobs new installed res heat per techn':
    'd_jobs_new_installed_res_heat_per_techn',
    'd jobs fuel supply solids bioe':
    'd_jobs_fuel_supply_solids_bioe',
    'new capacity installed growth rate res elec':
    'new_capacity_installed_growth_rate_res_elec',
    'employment factor fuel supply solids bioe':
    'employment_factor_fuel_supply_solids_bioe',
    'exogenous growth gtl':
    'exogenous_growth_gtl',
    'replacement gtl':
    'replacement_gtl',
    'crash programme gtl quest':
    'crash_programme_gtl_quest',
    'exogenous growth ctl':
    'exogenous_growth_ctl',
    'replacement ctl':
    'replacement_ctl',
    'aux12':
    'aux12',
    'coal to leave underground':
    'coal_to_leave_underground',
    'rurr coal start year plg':
    'rurr_coal_start_year_plg',
    'rurr conv oil until start year plg':
    'rurr_conv_oil_until_start_year_plg',
    'conv gas to leave underground':
    'conv_gas_to_leave_underground',
    'conv oil to leave underground':
    'conv_oil_to_leave_underground',
    'rurr unconv oil until start year plg':
    'rurr_unconv_oil_until_start_year_plg',
    'rurr unconv gas until start year plg':
    'rurr_unconv_gas_until_start_year_plg',
    'unconv gas to leave underground':
    'unconv_gas_to_leave_underground',
    'tot agg gas to leave underground':
    'tot_agg_gas_to_leave_underground',
    'unconv oil to leave underground':
    'unconv_oil_to_leave_underground',
    'aux11':
    'aux11',
    'tot agg oil to leave underground':
    'tot_agg_oil_to_leave_underground',
    'aux6':
    'aux6',
    'aux7':
    'aux7',
    'aux8':
    'aux8',
    'aux9':
    'aux9',
    'rurr conv gas until start year plg':
    'rurr_conv_gas_until_start_year_plg',
    'aux10':
    'aux10',
    'rurr tot gas until start year plg':
    'rurr_tot_gas_until_start_year_plg',
    'rurr tot oil until start year plg':
    'rurr_tot_oil_until_start_year_plg',
    'share elec demand covered by res':
    'share_elec_demand_covered_by_res',
    'rurr conv gas':
    'rurr_conv_gas',
    'rurr unconv gas':
    'rurr_unconv_gas',
    'rurr conv oil':
    'rurr_conv_oil',
    'variation share transm and distr losses elec':
    'variation_share_transm_and_distr_losses_elec',
    'share demand solids in transport':
    'share_demand_solids_in_transport',
    'share demand gas in transport':
    'share_demand_gas_in_transport',
    'share demand by fuel in transport':
    'share_demand_by_fuel_in_transport',
    'share demand electricity in transport':
    'share_demand_electricity_in_transport',
    'share demand heat in transport':
    'share_demand_heat_in_transport',
    'share demand liquids in transport':
    'share_demand_liquids_in_transport',
    'co2 emissions per value added':
    'co2_emissions_per_value_added',
    'liquids per x bus':
    'liquids_per_x_bus',
    'liquids per x hv':
    'liquids_per_x_hv',
    'liquids per x lv':
    'liquids_per_x_lv',
    'energy per x train':
    'energy_per_x_train',
    'adjust energy for transport to inland transport':
    'adjust_energy_for_transport_to_inland_transport',
    'effects shortage elec on ev div hib':
    'effects_shortage_elec_on_ev_div_hib',
    'hist var percent h':
    'hist_var_percent_h',
    'required number standard batteries':
    'required_number_standard_batteries',
    'transport tfed energy intensity':
    'transport_tfed_energy_intensity',
    'total number light vehicles':
    'total_number_light_vehicles',
    'transport tfed':
    'transport_tfed',
    'real fe consumption liquids ej':
    'real_fe_consumption_liquids_ej',
    'co2 emissions unconv gas':
    'co2_emissions_unconv_gas',
    'phase out oil for electricity quest':
    'phase_out_oil_for_electricity_quest',
    'max solar on land mha':
    'max_solar_on_land_mha',
    'max solar pv on land mha':
    'max_solar_pv_on_land_mha',
    'max solar pv on land twe':
    'max_solar_pv_on_land_twe',
    'total ch4 emissions fossil fuels':
    'total_ch4_emissions_fossil_fuels',
    'max csp on land mha':
    'max_csp_on_land_mha',
    'max csp twe':
    'max_csp_twe',
    'gch4 per mj gtl':
    'gch4_per_mj_gtl',
    'ch4 emissions gtl':
    'ch4_emissions_gtl',
    'ch4 emissions ctl':
    'ch4_emissions_ctl',
    'phase out oil for heat quest':
    'phase_out_oil_for_heat_quest',
    'gch4 per mj ctl':
    'gch4_per_mj_ctl',
    'g per gt':
    'g_per_gt',
    'bioe co2 emissions':
    'bioe_co2_emissions',
    'maximum 2w':
    'maximum_2w',
    'p h vehicle':
    'p_h_vehicle',
    'solid biofuels emissions relevant ej':
    'solid_biofuels_emissions_relevant_ej',
    'eroist system until 2015':
    'eroist_system_until_2015',
    'remaining potential elec storage by res techn':
    'remaining_potential_elec_storage_by_res_techn',
    'cp hydro 2015':
    'cp_hydro_2015',
    'esoi phs full potential':
    'esoi_phs_full_potential',
    'max capacity elec storage':
    'max_capacity_elec_storage',
    'cc impacts feedback shortage coeff':
    'cc_impacts_feedback_shortage_coeff',
    'eol rr minerals alt techn res vsx total economy':
    'eol_rr_minerals_alt_techn_res_vsx_total_economy',
    'crash programme ctl quest':
    'crash_programme_ctl_quest',
    'recycling rates minerals rest':
    'recycling_rates_minerals_rest',
    'p elec':
    'p_elec',
    'percents h vehicles':
    'percents_h_vehicles',
    't hist h transp':
    't_hist_h_transp',
    'bat number 2w':
    'bat_number_2w',
    'bateries ratio 2w e':
    'bateries_ratio_2w_e',
    'bat number ev':
    'bat_number_ev',
    'bat number hib':
    'bat_number_hib',
    'bateries ratio bus e':
    'bateries_ratio_bus_e',
    'bateries ratio hib bus':
    'bateries_ratio_hib_bus',
    'bateries ratio hib hv':
    'bateries_ratio_hib_hv',
    'bateries ratio hib lv':
    'bateries_ratio_hib_lv',
    'total number hybrid light vehicles':
    'total_number_hybrid_light_vehicles',
    'total number elec light vehicles':
    'total_number_elec_light_vehicles',
    'total number gas light vehicles':
    'total_number_gas_light_vehicles',
    'ev batteries tw':
    'ev_batteries_tw',
    'var percent t vehicles':
    'var_percent_t_vehicles',
    'p train elec':
    'p_train_elec',
    'p hv gas':
    'p_hv_gas',
    't ini inlandt':
    't_ini_inlandt',
    'p inlandt':
    'p_inlandt',
    'activate policy inlandt':
    'activate_policy_inlandt',
    'p lv elec':
    'p_lv_elec',
    'p lv hyb':
    'p_lv_hyb',
    'p bus elec':
    'p_bus_elec',
    'p bus gas':
    'p_bus_gas',
    'p bus hyb':
    'p_bus_hyb',
    'percents bus':
    'percents_bus',
    'percents train':
    'percents_train',
    'p hv hyb':
    'p_hv_hyb',
    'adapt var inlandt':
    'adapt_var_inlandt',
    'percents lv':
    'percents_lv',
    'var i inland elec':
    'var_i_inland_elec',
    'var i inlandt gas':
    'var_i_inlandt_gas',
    'var i inlandt liq':
    'var_i_inlandt_liq',
    'shares available t':
    'shares_available_t',
    'vehicles inlandt':
    'vehicles_inlandt',
    'percent t vehicles':
    'percent_t_vehicles',
    'efects shortage inlandt':
    'efects_shortage_inlandt',
    'p lv gas':
    'p_lv_gas',
    'percents hv':
    'percents_hv',
    'initial xt inland':
    'initial_xt_inland',
    'nx bus inlandt':
    'nx_bus_inlandt',
    'nx hv inland t':
    'nx_hv_inland_t',
    'nx lv inland t':
    'nx_lv_inland_t',
    'n vehicles inland t 0':
    'n_vehicles_inland_t_0',
    'energy initial inland transport':
    'energy_initial_inland_transport',
    'energy per x t':
    'energy_per_x_t',
    'nx train inland t':
    'nx_train_inland_t',
    'a2 coef th':
    'a2_coef_th',
    'h gas adapt growth':
    'h_gas_adapt_growth',
    'h hyb adapt growth':
    'h_hyb_adapt_growth',
    'activate policy h transp':
    'activate_policy_h_transp',
    'initial energy intensity of households transport 2009':
    'initial_energy_intensity_of_households_transport_2009',
    'h ev adapt growth':
    'h_ev_adapt_growth',
    'var ih e2':
    'var_ih_e2',
    'var ih gas2':
    'var_ih_gas2',
    'a1 coef th':
    'a1_coef_th',
    'var ih liq2':
    'var_ih_liq2',
    'percent h vehicles initial':
    'percent_h_vehicles_initial',
    'energy intensity of households transport':
    'energy_intensity_of_households_transport',
    'h 2we adapt growth':
    'h_2we_adapt_growth',
    'liq 4w':
    'liq_4w',
    'percent 2w liq':
    'percent_2w_liq',
    'percent 4w liq':
    'percent_4w_liq',
    'electricity 2we':
    'electricity_2we',
    'n vehicles h':
    'n_vehicles_h',
    'demand h':
    'demand_h',
    'ratio n veh demand h':
    'ratio_n_veh_demand_h',
    'percents 2w h vehicles':
    'percents_2w_h_vehicles',
    'percents 4w h vehicles':
    'percents_4w_h_vehicles',
    'p 2we':
    'p_2we',
    'max percent 2 wheels':
    'max_percent_2_wheels',
    'max percent 4 wheels':
    'max_percent_4_wheels',
    'aux hist h':
    'aux_hist_h',
    'p gas':
    'p_gas',
    'p share 2 wheelers':
    'p_share_2_wheelers',
    'p hyb':
    'p_hyb',
    'initial 2w percent':
    'initial_2w_percent',
    'share available 2w':
    'share_available_2w',
    'rate 4w to 2w':
    'rate_4w_to_2w',
    'share feh over fed by final fuel':
    'share_feh_over_fed_by_final_fuel',
    'share feh over fed oil':
    'share_feh_over_fed_oil',
    'share feh over fed coal':
    'share_feh_over_fed_coal',
    'share feh over fed natx gas':
    'share_feh_over_fed_natx_gas',
    'pes oil ej delayed':
    'pes_oil_ej_delayed',
    'energy required for material consumption for ev batteries':
    'energy_required_for_material_consumption_for_ev_batteries',
    'variation energy intensity of households transport':
    'variation_energy_intensity_of_households_transport',
    'number vehicles h':
    'number_vehicles_h',
    'effects shortage elec on ev':
    'effects_shortage_elec_on_ev',
    'effects shortage gas h veh':
    'effects_shortage_gas_h_veh',
    'xax extraction projection minerals':
    'xax_extraction_projection_minerals',
    'xbx extraction projection minerals':
    'xbx_extraction_projection_minerals',
    'variation minerals extraction rest':
    'variation_minerals_extraction_rest',
    'total recycled materials for other mt':
    'total_recycled_materials_for_other_mt',
    'share minerals consumption alt techn vs total economy':
    'share_minerals_consumption_alt_techn_vs_total_economy',
    'labor share cte quest':
    'labor_share_cte_quest',
    'initial minerals extraction rest':
    'initial_minerals_extraction_rest',
    'minerals extraction projection rest cte rr':
    'minerals_extraction_projection_rest_cte_rr',
    'materials to extract rest mt':
    'materials_to_extract_rest_mt',
    'minerals extraction projection rest with rr':
    'minerals_extraction_projection_rest_with_rr',
    'minerals consumption estimation rest cte rr':
    'minerals_consumption_estimation_rest_cte_rr',
    'total materials required for res elec plus ev batteries mt':
    'total_materials_required_for_res_elec_plus_ev_batteries_mt',
    'variation non energy use':
    'variation_non_energy_use',
    'number 2w':
    'number_2w',
    'number 4w':
    'number_4w',
    'number all':
    'number_all',
    'sum 4w shares':
    'sum_4w_shares',
    'share available 4w':
    'share_available_4w',
    'percent 4w':
    'percent_4w',
    'saving ratio 2we':
    'saving_ratio_2we',
    'percent all':
    'percent_all',
    'percent 2w':
    'percent_2w',
    'share fed coal vs nre heat nc':
    'share_fed_coal_vs_nre_heat_nc',
    'share fed gas vs nre heat nc':
    'share_fed_gas_vs_nre_heat_nc',
    'fed nre for heat nc':
    'fed_nre_for_heat_nc',
    'share fed liquids vs nre heat nc':
    'share_fed_liquids_vs_nre_heat_nc',
    'required fed by fuel':
    'required_fed_by_fuel',
    'bioe gen land marg available':
    'bioe_gen_land_marg_available',
    'potential peavail cellulosic biofuel ej':
    'potential_peavail_cellulosic_biofuel_ej',
    'potential peavail total biofuels':
    'potential_peavail_total_biofuels',
    'biofuels 3gen land compet available':
    'biofuels_3gen_land_compet_available',
    'fes total biofuels production ej':
    'fes_total_biofuels_production_ej',
    'fes total biofuels production ej 2':
    'fes_total_biofuels_production_ej_2',
    'fes total biofuels production mb div d':
    'fes_total_biofuels_production_mb_div_d',
    'peavail biofuels 2gen land compet ej':
    'peavail_biofuels_2gen_land_compet_ej',
    'peavail biofuels 3gen land compet ej':
    'peavail_biofuels_3gen_land_compet_ej',
    'peavail biofuels land marg ej':
    'peavail_biofuels_land_marg_ej',
    'pe biofuels land marg ej':
    'pe_biofuels_land_marg_ej',
    'pe biofuels prod x2gen plus x3gen ej':
    'pe_biofuels_prod_x2gen_plus_x3gen_ej',
    'pe biomass for biofuels production ej':
    'pe_biomass_for_biofuels_production_ej',
    'pe cellulosic biofuel ej':
    'pe_cellulosic_biofuel_ej',
    'max peavail biofuels potential':
    'max_peavail_biofuels_potential',
    'start year biofuels land marg':
    'start_year_biofuels_land_marg',
    'land required biofuels land marg':
    'land_required_biofuels_land_marg',
    'max peavail potential biofuels marginal lands':
    'max_peavail_potential_biofuels_marginal_lands',
    'share biofuels overcapacity':
    'share_biofuels_overcapacity',
    'total land requirements renew mha':
    'total_land_requirements_renew_mha',
    'land occupation ratio biofuels marg land':
    'land_occupation_ratio_biofuels_marg_land',
    'peavail cellulosic biofuel ej':
    'peavail_cellulosic_biofuel_ej',
    'potential peavail biofuels land marg ej':
    'potential_peavail_biofuels_land_marg_ej',
    'bioe potential npp marginal lands':
    'bioe_potential_npp_marginal_lands',
    'additional pe production of bioenergy for biofuels':
    'additional_pe_production_of_bioenergy_for_biofuels',
    'oil liquids saved by biofuels ej':
    'oil_liquids_saved_by_biofuels_ej',
    'efficiency bioe residues to cellulosic liquids':
    'efficiency_bioe_residues_to_cellulosic_liquids',
    'conv efficiency from npp to biofuels':
    'conv_efficiency_from_npp_to_biofuels',
    'pes heat res':
    'pes_heat_res',
    'ped nre liquids':
    'ped_nre_liquids',
    'potential fes ctl plus gtl ej':
    'potential_fes_ctl_plus_gtl_ej',
    'tfec res delayed 1yr':
    'tfec_res_delayed_1yr',
    'pe supply from res non elec without trad bioe ej':
    'pe_supply_from_res_non_elec_without_trad_bioe_ej',
    'pes gases':
    'pes_gases',
    'fes ctl plus gtl ej':
    'fes_ctl_plus_gtl_ej',
    'activate elf all scen quest':
    'activate_elf_all_scen_quest',
    'tpes res delayed 1yr':
    'tpes_res_delayed_1yr',
    'annual tpes res growth rate':
    'annual_tpes_res_growth_rate',
    'ped natx gas ej':
    'ped_natx_gas_ej',
    'annual share res vs tfec growth rate':
    'annual_share_res_vs_tfec_growth_rate',
    'annual share res vs tpes growth rate':
    'annual_share_res_vs_tpes_growth_rate',
    'share res vs tpes delayed 1yr':
    'share_res_vs_tpes_delayed_1yr',
    'gtl production':
    'gtl_production',
    'pes biogas for tfc':
    'pes_biogas_for_tfc',
    'share ctl plus gtl overcapacity':
    'share_ctl_plus_gtl_overcapacity',
    'share res vs tfec delayed 1yr':
    'share_res_vs_tfec_delayed_1yr',
    'share e losses cc':
    'share_e_losses_cc',
    'ped natx gas for gtl ej':
    'ped_natx_gas_for_gtl_ej',
    'ped coal for ctl ej':
    'ped_coal_for_ctl_ej',
    'annual tfec res growth rate':
    'annual_tfec_res_growth_rate',
    'ped total oil ej':
    'ped_total_oil_ej',
    'ctl production':
    'ctl_production',
    'ch4 emissions coal without ctl':
    'ch4_emissions_coal_without_ctl',
    'pes tot res for heat':
    'pes_tot_res_for_heat',
    'total fe real supply res for heat nc ej':
    'total_fe_real_supply_res_for_heat_nc_ej',
    'real extraction conv oil emissions relevant ej':
    'real_extraction_conv_oil_emissions_relevant_ej',
    'co2 emissions coal without ctl':
    'co2_emissions_coal_without_ctl',
    'real extraction conv gas emissions relevant ej':
    'real_extraction_conv_gas_emissions_relevant_ej',
    'pes res for heat nc by techn':
    'pes_res_for_heat_nc_by_techn',
    'fes nre for heat':
    'fes_nre_for_heat',
    'installed capacity res heat nc tw':
    'installed_capacity_res_heat_nc_tw',
    'fed heat com plants fossil fuels ej':
    'fed_heat_com_plants_fossil_fuels_ej',
    'real extraction unconv gas emissions relevant ej':
    'real_extraction_unconv_gas_emissions_relevant_ej',
    'real extraction unconv oil emissions relevant ej':
    'real_extraction_unconv_oil_emissions_relevant_ej',
    'available pe potential solid bioe for elec ej':
    'available_pe_potential_solid_bioe_for_elec_ej',
    'remaining potential res for heat':
    'remaining_potential_res_for_heat',
    'extraction coal emissions relevant ej':
    'extraction_coal_emissions_relevant_ej',
    'wear res capacity for heat nc tw':
    'wear_res_capacity_for_heat_nc_tw',
    'fe real generation res heat nc ej':
    'fe_real_generation_res_heat_nc_ej',
    'total fe real supply res for heat com ej':
    'total_fe_real_supply_res_for_heat_com_ej',
    'past res growth for heat com x0':
    'past_res_growth_for_heat_com_x0',
    'efficiency conversion bioe plants to heat 0':
    'efficiency_conversion_bioe_plants_to_heat_0',
    'fed heat com after priorities ej':
    'fed_heat_com_after_priorities_ej',
    'fes heat from biow':
    'fes_heat_from_biow',
    'abundance res heat nc':
    'abundance_res_heat_nc',
    'efficiency geothermal for heat 0':
    'efficiency_geothermal_for_heat_0',
    'fes heat com nuclear chp plants ej':
    'fes_heat_com_nuclear_chp_plants_ej',
    'fe real supply res for heat nc tot ej':
    'fe_real_supply_res_for_heat_nc_tot_ej',
    'initial value res for heat nc':
    'initial_value_res_for_heat_nc',
    'past res growth for heat nc':
    'past_res_growth_for_heat_nc',
    'p solid bioe for heat 0':
    'p_solid_bioe_for_heat_0',
    'fed heat fossil fuels chp plants ej':
    'fed_heat_fossil_fuels_chp_plants_ej',
    'replacement res for heat nc':
    'replacement_res_for_heat_nc',
    'efficiency solar panels for heat 0':
    'efficiency_solar_panels_for_heat_0',
    'p res for heat 0':
    'p_res_for_heat_0',
    'p solar for heat 0':
    'p_solar_for_heat_0',
    'abundance res heat com':
    'abundance_res_heat_com',
    'abundance res heat nc2':
    'abundance_res_heat_nc2',
    'potential fes tot res for heat nc ej':
    'potential_fes_tot_res_for_heat_nc_ej',
    'life time res for heat 0':
    'life_time_res_for_heat_0',
    'efficiency res heat 0':
    'efficiency_res_heat_0',
    'replacement res for heat 0':
    'replacement_res_for_heat_0',
    'p geothermal for heat 0':
    'p_geothermal_for_heat_0',
    'fes res for heat ej':
    'fes_res_for_heat_ej',
    'fe real supply res for heat com tot ej':
    'fe_real_supply_res_for_heat_com_tot_ej',
    'losses solar for heat 0':
    'losses_solar_for_heat_0',
    'res heat nc tot overcapacity':
    'res_heat_nc_tot_overcapacity',
    'potential fes res for heat nc ej':
    'potential_fes_res_for_heat_nc_ej',
    'other solids required':
    'other_solids_required',
    'other gases required':
    'other_gases_required',
    'transformation ff losses ej':
    'transformation_ff_losses_ej',
    'fes elec fossil fuel chp plants ej':
    'fes_elec_fossil_fuel_chp_plants_ej',
    'total fe elec demand after priorities twh':
    'total_fe_elec_demand_after_priorities_twh',
    'demand elec nre twh':
    'demand_elec_nre_twh',
    'non energy use demand by final fuel ej':
    'non_energy_use_demand_by_final_fuel_ej',
    'share solids for final energy':
    'share_solids_for_final_energy',
    'real fe consumption gases ej':
    'real_fe_consumption_gases_ej',
    'total real non energy use consumption ej':
    'total_real_non_energy_use_consumption_ej',
    'share gases for final energy':
    'share_gases_for_final_energy',
    'ratio fed for heat nc vs fed for heat com':
    'ratio_fed_for_heat_nc_vs_fed_for_heat_com',
    'real fe consumption by fuel before heat correction':
    'real_fe_consumption_by_fuel_before_heat_correction',
    'required tfed before heat dem corr':
    'required_tfed_before_heat_dem_corr',
    'cum materials to extract for ev batteries':
    'cum_materials_to_extract_for_ev_batteries',
    'share cum dem materials to extract alt techn vs total':
    'share_cum_dem_materials_to_extract_alt_techn_vs_total',
    'total recycled materials for ev batteries mt':
    'total_recycled_materials_for_ev_batteries_mt',
    'share res vs tfec':
    'share_res_vs_tfec',
    'cum materials to extract for alt techn from 2015':
    'cum_materials_to_extract_for_alt_techn_from_2015',
    'total materials to extract for ev batteries from 2015 mt':
    'total_materials_to_extract_for_ev_batteries_from_2015_mt',
    'materials per new capacity installed ev batteries':
    'materials_per_new_capacity_installed_ev_batteries',
    'total materials to extract for ev batteries mt':
    'total_materials_to_extract_for_ev_batteries_mt',
    'total materials to extract mt':
    'total_materials_to_extract_mt',
    'cum materials requirements for ev batteries':
    'cum_materials_requirements_for_ev_batteries',
    'xstaticx eroigrid res elec':
    'xstaticx_eroigrid_res_elec',
    't per x':
    't_per_x',
    'total materials required for ev batteries':
    'total_materials_required_for_ev_batteries',
    'tfec from res per capita':
    'tfec_from_res_per_capita',
    'share materials cum demand to extract vs reserves for res elec':
    'share_materials_cum_demand_to_extract_vs_reserves_for_res_elec',
    'rt storage efficiency ev batteries':
    'rt_storage_efficiency_ev_batteries',
    'cum materials to extract for ev batteries from 2015':
    'cum_materials_to_extract_for_ev_batteries_from_2015',
    'total cumulative demand materials to extract from 2015':
    'total_cumulative_demand_materials_to_extract_from_2015',
    'initial cumulated material requirements for ev batteries 1995':
    'initial_cumulated_material_requirements_for_ev_batteries_1995',
    'share materials cum demand to extract vs resources for res elec':
    'share_materials_cum_demand_to_extract_vs_resources_for_res_elec',
    'fe tot generation all res elec ej':
    'fe_tot_generation_all_res_elec_ej',
    'carbon footprint tonnesc div person':
    'carbon_footprint_tonnesc_div_person',
    'potential max hdi':
    'potential_max_hdi',
    'kw per battery ev':
    'kw_per_battery_ev',
    'pes fossil fuel extraction delayed':
    'pes_fossil_fuel_extraction_delayed',
    'energy distr losses ff ej':
    'energy_distr_losses_ff_ej',
    'pes fossil fuel extraction':
    'pes_fossil_fuel_extraction',
    'share conv vs total oil extraction':
    'share_conv_vs_total_oil_extraction',
    'pes natx gas without gtl':
    'pes_natx_gas_without_gtl',
    'co2 emissions conv gas without gtl':
    'co2_emissions_conv_gas_without_gtl',
    'co2 emissions conv oil':
    'co2_emissions_conv_oil',
    'co2 emissions gtl':
    'co2_emissions_gtl',
    'ch4 emissions conv gas without gtl':
    'ch4_emissions_conv_gas_without_gtl',
    'co2 emissions unconv oil':
    'co2_emissions_unconv_oil',
    'share conv vs total gas extraction':
    'share_conv_vs_total_gas_extraction',
    'ch4 emissions unconv gas':
    'ch4_emissions_unconv_gas',
    'fe heat demand consum':
    'fe_heat_demand_consum',
    'share electricity vs tfes':
    'share_electricity_vs_tfes',
    'co2 emissions peat':
    'co2_emissions_peat',
    'required fed by gas':
    'required_fed_by_gas',
    'required tfed':
    'required_tfed',
    'total fe elec consumption ej':
    'total_fe_elec_consumption_ej',
    'total fe elec consumption twh':
    'total_fe_elec_consumption_twh',
    'ped gases':
    'ped_gases',
    'total fe heat consumption ej':
    'total_fe_heat_consumption_ej',
    'share solids vs tfes':
    'share_solids_vs_tfes',
    'share gases vs tfes':
    'share_gases_vs_tfes',
    'required fed solids':
    'required_fed_solids',
    'share heat vs tfes':
    'share_heat_vs_tfes',
    'ped solids':
    'ped_solids',
    'scarcity conv oil':
    'scarcity_conv_oil',
    'share liquids vs tfes':
    'share_liquids_vs_tfes',
    'gfcf not covered':
    'gfcf_not_covered',
    'lc not covered':
    'lc_not_covered',
    'cc total not covered':
    'cc_total_not_covered',
    'household demand not covered':
    'household_demand_not_covered',
    'real total output inland transport':
    'real_total_output_inland_transport',
    'tfes intensity ej tdollar':
    'tfes_intensity_ej_tdollar',
    'tfes intensity ej tdollar delayed 1yr':
    'tfes_intensity_ej_tdollar_delayed_1yr',
    'tpes intensity ej tdollar delayed 1yr':
    'tpes_intensity_ej_tdollar_delayed_1yr',
    'annual tpes intensity growth rate':
    'annual_tpes_intensity_growth_rate',
    'annual tfes intensity growth rate':
    'annual_tfes_intensity_growth_rate',
    'total d jobs res elec per techn':
    'total_d_jobs_res_elec_per_techn',
    'total d jobs res heat per techn':
    'total_d_jobs_res_heat_per_techn',
    'employment factors new res elec':
    'employment_factors_new_res_elec',
    'employment factors new res heat':
    'employment_factors_new_res_heat',
    'employment factors o and m res elec':
    'employment_factors_o_and_m_res_elec',
    'employment factors o and m res heat':
    'employment_factors_o_and_m_res_heat',
    'd jobs new installed res elec per techn':
    'd_jobs_new_installed_res_elec_per_techn',
    'jobs o and m res elec per techn':
    'jobs_o_and_m_res_elec_per_techn',
    'nx0 vehicles per xinland t':
    'nx0_vehicles_per_xinland_t',
    'initial percent t vehicles':
    'initial_percent_t_vehicles',
    'saving ratios v':
    'saving_ratios_v',
    'share gases dem for heat nc':
    'share_gases_dem_for_heat_nc',
    'increase scarcity conv gas':
    'increase_scarcity_conv_gas',
    'scarcity conv gas stock':
    'scarcity_conv_gas_stock',
    'pes natx gas for heat nc plants':
    'pes_natx_gas_for_heat_nc_plants',
    'real growth ctl':
    'real_growth_ctl',
    'ctl potential production':
    'ctl_potential_production',
    'abundance liquids gtl':
    'abundance_liquids_gtl',
    'gtl potential production':
    'gtl_potential_production',
    'abundance liquids ctl':
    'abundance_liquids_ctl',
    'wear gtl':
    'wear_gtl',
    'lifetime gtl':
    'lifetime_gtl',
    'lifetime ctl':
    'lifetime_ctl',
    'wear ctl':
    'wear_ctl',
    'abundance unconv oil stock':
    'abundance_unconv_oil_stock',
    'increase abundance unconv oil':
    'increase_abundance_unconv_oil',
    'abundance unconv oil':
    'abundance_unconv_oil',
    'abundance unconv oil delayed 1yr':
    'abundance_unconv_oil_delayed_1yr',
    'abundance unconv oil2':
    'abundance_unconv_oil2',
    'real extraction unconv oil ej':
    'real_extraction_unconv_oil_ej',
    'scarcity conv oil stock':
    'scarcity_conv_oil_stock',
    'share variable res elec generation vs total gen':
    'share_variable_res_elec_generation_vs_total_gen',
    'extra monet invest to cope with variable elec res':
    'extra_monet_invest_to_cope_with_variable_elec_res',
    'increase scarcity conv oil':
    'increase_scarcity_conv_oil',
    'share extra monet invest to cope with variable elec res':
    'share_extra_monet_invest_to_cope_with_variable_elec_res',
    'initial share variable res elec gen vs total':
    'initial_share_variable_res_elec_gen_vs_total',
    'pes oil for heat nc plants':
    'pes_oil_for_heat_nc_plants',
    'cumulated invest e grid':
    'cumulated_invest_e_grid',
    'total monet invest res for elec tdolar':
    'total_monet_invest_res_for_elec_tdolar',
    'cp exogenous res elec var reduction':
    'cp_exogenous_res_elec_var_reduction',
    'cp exogenous res elec dispatch reduction':
    'cp_exogenous_res_elec_dispatch_reduction',
    'increase variable res share elec vs total generation':
    'increase_variable_res_share_elec_vs_total_generation',
    'pes nre heat nc':
    'pes_nre_heat_nc',
    'tpes heat':
    'tpes_heat',
    'pes nre heat':
    'pes_nre_heat',
    'share liquids dem for heat nc':
    'share_liquids_dem_for_heat_nc',
    'pes nre heat com':
    'pes_nre_heat_com',
    'check tpe':
    'check_tpe',
    'fed by fuel for heat nc':
    'fed_by_fuel_for_heat_nc',
    'share fed heat com vs total heat':
    'share_fed_heat_com_vs_total_heat',
    'average elec consumption per capita':
    'average_elec_consumption_per_capita',
    'fed solid bioe for heat nc':
    'fed_solid_bioe_for_heat_nc',
    'total fed heat ej':
    'total_fed_heat_ej',
    'heat nc distribution losses':
    'heat_nc_distribution_losses',
    'total fed heat nc ej':
    'total_fed_heat_nc_ej',
    'total fed nre heat nc':
    'total_fed_nre_heat_nc',
    'deactivate heat dem correction quest':
    'deactivate_heat_dem_correction_quest',
    'share feh over fed solid bioe':
    'share_feh_over_fed_solid_bioe',
    'abundance heat':
    'abundance_heat',
    'pes coal for heat nc plants':
    'pes_coal_for_heat_nc_plants',
    'required fed sectors by fuel':
    'required_fed_sectors_by_fuel',
    'share trad biomass vs solids in households':
    'share_trad_biomass_vs_solids_in_households',
    'share global pop dependent on trad biomass':
    'share_global_pop_dependent_on_trad_biomass',
    'pes oil for heat com plants':
    'pes_oil_for_heat_com_plants',
    'share coal dem for heat nc':
    'share_coal_dem_for_heat_nc',
    'res heat com tot overcapacity':
    'res_heat_com_tot_overcapacity',
    'pes natx gas for heat com plants':
    'pes_natx_gas_for_heat_com_plants',
    'pes coal for heat com plants':
    'pes_coal_for_heat_com_plants',
    'required heat com':
    'required_heat_com',
    'variation labour share':
    'variation_labour_share',
    'variation household demand':
    'variation_household_demand',
    'labour share':
    'labour_share',
    'capital share':
    'capital_share',
    'growth capital share':
    'growth_capital_share',
    'include materials for overgrids quest':
    'include_materials_for_overgrids_quest',
    'all minerals virgin quest':
    'all_minerals_virgin_quest',
    'materials for new res elec per capacity installed':
    'materials_for_new_res_elec_per_capacity_installed',
    'cedtot per material res elec var':
    'cedtot_per_material_res_elec_var',
    'cedtot per tw res elec var':
    'cedtot_per_tw_res_elec_var',
    'cedtot per tw per material res elec var':
    'cedtot_per_tw_per_material_res_elec_var',
    'demand by sector fd':
    'demand_by_sector_fd',
    'sum variation':
    'sum_variation',
    'cc sectoral next step':
    'cc_sectoral_next_step',
    'gross fixed capital formation':
    'gross_fixed_capital_formation',
    'pct gfcf vs gfcf plus hd':
    'pct_gfcf_vs_gfcf_plus_hd',
    'household demand':
    'household_demand',
    'lc next step':
    'lc_next_step',
    'household demand total':
    'household_demand_total',
    'cedtot per tw over lifetime res elec dispatch':
    'cedtot_per_tw_over_lifetime_res_elec_dispatch',
    'quality of electricity 2015':
    'quality_of_electricity_2015',
    'dynamic quality of electricity':
    'dynamic_quality_of_electricity',
    'quality of electricity':
    'quality_of_electricity',
    'cp exogenous res elec reduction':
    'cp_exogenous_res_elec_reduction',
    'res elec variables quest':
    'res_elec_variables_quest',
    'aux3':
    'aux3',
    'fei res elec var':
    'fei_res_elec_var',
    'xstaticx eroi res elec':
    'xstaticx_eroi_res_elec',
    'materials required for new res elec mt':
    'materials_required_for_new_res_elec_mt',
    'fei over lifetime res elec var':
    'fei_over_lifetime_res_elec_var',
    'ced decom res elec capacity':
    'ced_decom_res_elec_capacity',
    'ced o and m per material res elec var':
    'ced_o_and_m_per_material_res_elec_var',
    'cedtot new cap res elec var':
    'cedtot_new_cap_res_elec_var',
    'cedtot o and m res elec var':
    'cedtot_o_and_m_res_elec_var',
    'aux1':
    'aux1',
    'b lineal regr':
    'b_lineal_regr',
    'a lineal regr':
    'a_lineal_regr',
    'esoi phs depleted potential':
    'esoi_phs_depleted_potential',
    'cc total':
    'cc_total',
    'initial household demand':
    'initial_household_demand',
    'total demand':
    'total_demand',
    'demand not covered by sector fd':
    'demand_not_covered_by_sector_fd',
    'initial demand by sectot':
    'initial_demand_by_sectot',
    'beta 1 lab':
    'beta_1_lab',
    'initial lc total':
    'initial_lc_total',
    'initial gfcf':
    'initial_gfcf',
    'beta 0 cap':
    'beta_0_cap',
    'initial cc total':
    'initial_cc_total',
    'beta 2 cap':
    'beta_2_cap',
    'demand not covered total fd':
    'demand_not_covered_total_fd',
    'beta 1 cap':
    'beta_1_cap',
    'lc':
    'lc',
    'bet 0 lab':
    'bet_0_lab',
    'tped by fuel':
    'tped_by_fuel',
    'abundance tpe':
    'abundance_tpe',
    'beta 2 lab':
    'beta_2_lab',
    'available pe potential solid bioe for heat ej':
    'available_pe_potential_solid_bioe_for_heat_ej',
    'max pe potential res for heat':
    'max_pe_potential_res_for_heat',
    'pes res for heat com by techn':
    'pes_res_for_heat_com_by_techn',
    'p res for heat':
    'p_res_for_heat',
    'fe real generation res heat com ej':
    'fe_real_generation_res_heat_com_ej',
    'potential fes tot res for heat com ej':
    'potential_fes_tot_res_for_heat_com_ej',
    'available potential fe solid bioe for elec ej':
    'available_potential_fe_solid_bioe_for_elec_ej',
    'max bioe twe':
    'max_bioe_twe',
    'remaining potential tot res heat':
    'remaining_potential_tot_res_heat',
    'potential fes heat com nuclear chp plants ej':
    'potential_fes_heat_com_nuclear_chp_plants_ej',
    'share of heat production in chp plants vs total nucelar elec generation':
    'share_of_heat_production_in_chp_plants_vs_total_nucelar_elec_generation',
    'pes waste for elec plants':
    'pes_waste_for_elec_plants',
    'losses chp biogas':
    'losses_chp_biogas',
    'losses chp waste':
    'losses_chp_waste',
    'share pes biogas for heat':
    'share_pes_biogas_for_heat',
    'pe losses res for elec':
    'pe_losses_res_for_elec',
    'pes tot waste for elec':
    'pes_tot_waste_for_elec',
    'pes tot waste for heat com':
    'pes_tot_waste_for_heat_com',
    'abundance res heat com2':
    'abundance_res_heat_com2',
    'max pe potential biogas for heat':
    'max_pe_potential_biogas_for_heat',
    'share efficiency biogas for elec in chp plants':
    'share_efficiency_biogas_for_elec_in_chp_plants',
    'share efficiency waste for elec in chp plants':
    'share_efficiency_waste_for_elec_in_chp_plants',
    'max potential pe non electric res':
    'max_potential_pe_non_electric_res',
    'pes tot biogas for elec':
    'pes_tot_biogas_for_elec',
    'pes tot biogas for heat com':
    'pes_tot_biogas_for_heat_com',
    'pe losses nre elec generation':
    'pe_losses_nre_elec_generation',
    'elec gen related losses ej':
    'elec_gen_related_losses_ej',
    'pe losses biogas for elec':
    'pe_losses_biogas_for_elec',
    'pe losses waste for elec':
    'pe_losses_waste_for_elec',
    'max pe potential tot res heat ej':
    'max_pe_potential_tot_res_heat_ej',
    'share pes biogas for elec':
    'share_pes_biogas_for_elec',
    'p hydro growth':
    'p_hydro_growth',
    'fe real tot generation res elec twh':
    'fe_real_tot_generation_res_elec_twh',
    'p solar pv growth':
    'p_solar_pv_growth',
    'remaining potential constraint on new res heat capacity':
    'remaining_potential_constraint_on_new_res_heat_capacity',
    'total fe elec generation twh':
    'total_fe_elec_generation_twh',
    'fe tot generation all res elec twh':
    'fe_tot_generation_all_res_elec_twh',
    'p oceanic growth':
    'p_oceanic_growth',
    'pe elec generation from res ej':
    'pe_elec_generation_from_res_ej',
    'p res elec growth':
    'p_res_elec_growth',
    'share res electricity generation':
    'share_res_electricity_generation',
    'p solid bioe elec growth':
    'p_solid_bioe_elec_growth',
    'p csp growth':
    'p_csp_growth',
    'remaining potential tot res elec':
    'remaining_potential_tot_res_elec',
    'p wind offshore growth':
    'p_wind_offshore_growth',
    'p wind onshore growth':
    'p_wind_onshore_growth',
    'elec generation dispatch from res twh':
    'elec_generation_dispatch_from_res_twh',
    'fes elec from res with priority twh':
    'fes_elec_from_res_with_priority_twh',
    'abundance res elec':
    'abundance_res_elec',
    'fes elec from biow':
    'fes_elec_from_biow',
    'p geot growth':
    'p_geot_growth',
    'max potential tot res elec twh':
    'max_potential_tot_res_elec_twh',
    'p solid bioe for heat':
    'p_solid_bioe_for_heat',
    'pe real generation res elec':
    'pe_real_generation_res_elec',
    'efficiency res heat':
    'efficiency_res_heat',
    'share oil dem for heat com':
    'share_oil_dem_for_heat_com',
    'fe elec generation from total oil twh':
    'fe_elec_generation_from_total_oil_twh',
    'total fe heat generation ej':
    'total_fe_heat_generation_ej',
    'share coal dem for elec':
    'share_coal_dem_for_elec',
    'pe losses oil for elec ej':
    'pe_losses_oil_for_elec_ej',
    'share oil dem for elec':
    'share_oil_dem_for_elec',
    'share coal dem for heat com':
    'share_coal_dem_for_heat_com',
    'fe elec generation from conv gas twh':
    'fe_elec_generation_from_conv_gas_twh',
    'share res heat generation':
    'share_res_heat_generation',
    'share natx gas dem for elec':
    'share_natx_gas_dem_for_elec',
    'pe losses conv gas for elec ej':
    'pe_losses_conv_gas_for_elec_ej',
    'pe losses coal for elec ej':
    'pe_losses_coal_for_elec_ej',
    'fe elec generation from coal twh':
    'fe_elec_generation_from_coal_twh',
    'share natx gas dem for heat com':
    'share_natx_gas_dem_for_heat_com',
    'year scarcity heat':
    'year_scarcity_heat',
    'fes heat com from biogas in chp plants':
    'fes_heat_com_from_biogas_in_chp_plants',
    'efficiency biogas for heat plants':
    'efficiency_biogas_for_heat_plants',
    'fes elec from biogas in chp plants':
    'fes_elec_from_biogas_in_chp_plants',
    'fes elec from biogas ej':
    'fes_elec_from_biogas_ej',
    'pes biogas for heat com plants':
    'pes_biogas_for_heat_com_plants',
    'fes elec from biogas in elec plants':
    'fes_elec_from_biogas_in_elec_plants',
    'efficiency biogas for elec plants':
    'efficiency_biogas_for_elec_plants',
    'fes biogas for heat com plants':
    'fes_biogas_for_heat_com_plants',
    'pes biogas for elec plants':
    'pes_biogas_for_elec_plants',
    'share pes biogas tfc':
    'share_pes_biogas_tfc',
    'potential pes biogas for tfc':
    'potential_pes_biogas_for_tfc',
    'fes elec from biogas twh':
    'fes_elec_from_biogas_twh',
    'pes biogas for chp':
    'pes_biogas_for_chp',
    'share pes biogas for heat com plants':
    'share_pes_biogas_for_heat_com_plants',
    'efficiency biogas for elec chp plants':
    'efficiency_biogas_for_elec_chp_plants',
    'fes heat com from biogas ej':
    'fes_heat_com_from_biogas_ej',
    'efficiency biogas for heat chp plants':
    'efficiency_biogas_for_heat_chp_plants',
    'share pes biogas for elec plants':
    'share_pes_biogas_for_elec_plants',
    'share pes biogas for chp':
    'share_pes_biogas_for_chp',
    'demand elec plants fossil fuels twh':
    'demand_elec_plants_fossil_fuels_twh',
    'total extraction nre ej':
    'total_extraction_nre_ej',
    'constrain rr improv for alt techn per mineral':
    'constrain_rr_improv_for_alt_techn_per_mineral',
    'constrain rr improv for rest per mineral':
    'constrain_rr_improv_for_rest_per_mineral',
    'ced o and m over lifetime per material res elec var':
    'ced_o_and_m_over_lifetime_per_material_res_elec_var',
    'energy cons per unit of material cons for res elec':
    'energy_cons_per_unit_of_material_cons_for_res_elec',
    'ced new cap per material res elec var':
    'ced_new_cap_per_material_res_elec_var',
    'energy required for material consumption for new res elec':
    'energy_required_for_material_consumption_for_new_res_elec',
    'energy required for material consumption for o and m res elec':
    'energy_required_for_material_consumption_for_o_and_m_res_elec',
    'share other cumulative demand to extract vs resources materials':
    'share_other_cumulative_demand_to_extract_vs_resources_materials',
    'materials to extract rest from 2015 mt':
    'materials_to_extract_rest_from_2015_mt',
    'total recycled materials for res elec mt':
    'total_recycled_materials_for_res_elec_mt',
    'cum materials to extract rest':
    'cum_materials_to_extract_rest',
    'cum materials to extract rest from 2015':
    'cum_materials_to_extract_rest_from_2015',
    'share other cumulative demand to extract vs reserves materials':
    'share_other_cumulative_demand_to_extract_vs_reserves_materials',
    'materials availability xannual extractionx':
    'materials_availability_xannual_extractionx',
    'mt per tonne':
    'mt_per_tonne',
    'initial cumulated material requirements for rest 1995':
    'initial_cumulated_material_requirements_for_rest_1995',
    'p common rr minerals variation rest':
    'p_common_rr_minerals_variation_rest',
    'cum materials to extract for res elec from 2015':
    'cum_materials_to_extract_for_res_elec_from_2015',
    'total materials to extract for res elec mt':
    'total_materials_to_extract_for_res_elec_mt',
    'cum materials to extract for res elec':
    'cum_materials_to_extract_for_res_elec',
    'total materials to extract for res elec from 2015 mt':
    'total_materials_to_extract_for_res_elec_from_2015_mt',
    'max recycling rates minerals':
    'max_recycling_rates_minerals',
    'p common rr minerals variation alt techn':
    'p_common_rr_minerals_variation_alt_techn',
    'current recycling rates minerals':
    'current_recycling_rates_minerals',
    'historic improvement recycling rates minerals':
    'historic_improvement_recycling_rates_minerals',
    'initial energy cons per unit of material cons xrecycledx':
    'initial_energy_cons_per_unit_of_material_cons_xrecycledx',
    'materials required for o and m res elec mt':
    'materials_required_for_o_and_m_res_elec_mt',
    'share tot cum dem vs reserves materials':
    'share_tot_cum_dem_vs_reserves_materials',
    'share tot cum dem vs resources materials':
    'share_tot_cum_dem_vs_resources_materials',
    'maximum annual extraction materials':
    'maximum_annual_extraction_materials',
    'materials availability xresourcesx':
    'materials_availability_xresourcesx',
    'materials availability xreservesx':
    'materials_availability_xreservesx',
    'tpes ej':
    'tpes_ej',
    'fes heat com from waste ej':
    'fes_heat_com_from_waste_ej',
    'fes waste for heat com plants':
    'fes_waste_for_heat_com_plants',
    'fes elec from waste in chp plants':
    'fes_elec_from_waste_in_chp_plants',
    'fes elec from waste in elec plants':
    'fes_elec_from_waste_in_elec_plants',
    'fes heat com from waste in chp plants':
    'fes_heat_com_from_waste_in_chp_plants',
    'pes waste for heat com plants':
    'pes_waste_for_heat_com_plants',
    'share pes waste for heat com plants':
    'share_pes_waste_for_heat_com_plants',
    'share pes waste tfc':
    'share_pes_waste_tfc',
    'share pes waste for chp':
    'share_pes_waste_for_chp',
    'share pes waste for elec plants':
    'share_pes_waste_for_elec_plants',
    'waste change':
    'waste_change',
    'fes elec from waste ej':
    'fes_elec_from_waste_ej',
    'fes elec from waste twh':
    'fes_elec_from_waste_twh',
    'efficiency waste for elec plants':
    'efficiency_waste_for_elec_plants',
    'pes waste ej':
    'pes_waste_ej',
    'pes waste for chp plants':
    'pes_waste_for_chp_plants',
    'efficiency waste for elec chp plants':
    'efficiency_waste_for_elec_chp_plants',
    'initial pes waste':
    'initial_pes_waste',
    'pes waste for tfc':
    'pes_waste_for_tfc',
    'efficiency waste for heat chp plants':
    'efficiency_waste_for_heat_chp_plants',
    'p waste change':
    'p_waste_change',
    'efficiency waste for heat plants':
    'efficiency_waste_for_heat_plants',
    'max waste':
    'max_waste',
    'pes solids bioe and waste ej':
    'pes_solids_bioe_and_waste_ej',
    'past waste growth':
    'past_waste_growth',
    'ch4 emissions oil':
    'ch4_emissions_oil',
    'gch4 per mj coal':
    'gch4_per_mj_coal',
    'gch4 per mj oil':
    'gch4_per_mj_oil',
    'fe elec generation from fossil fuels twh':
    'fe_elec_generation_from_fossil_fuels_twh',
    'pe demand uranium ej':
    'pe_demand_uranium_ej',
    'fes elec fossil fuel chp plants twh':
    'fes_elec_fossil_fuel_chp_plants_twh',
    'fes heat com fossil fuels chp plants ej':
    'fes_heat_com_fossil_fuels_chp_plants_ej',
    'potential generation nuclear elec twh':
    'potential_generation_nuclear_elec_twh',
    'threshold remaining potential new capacity':
    'threshold_remaining_potential_new_capacity',
    'installed capacity res elec tw':
    'installed_capacity_res_elec_tw',
    'total time plan plus constr res elec':
    'total_time_plan_plus_constr_res_elec',
    'new required capacity res elec':
    'new_required_capacity_res_elec',
    'initial capacity in construction res elec':
    'initial_capacity_in_construction_res_elec',
    'remaining potential constraint on new res elec capacity':
    'remaining_potential_constraint_on_new_res_elec_capacity',
    'required capacity res elec tw':
    'required_capacity_res_elec_tw',
    'res elec planned capacity tw':
    'res_elec_planned_capacity_tw',
    'initial energy cons per unit of material cons xrecycledx data':
    'initial_energy_cons_per_unit_of_material_cons_xrecycledx_data',
    'cp phs':
    'cp_phs',
    'max potential phs twe':
    'max_potential_phs_twe',
    'max capacity potential phs':
    'max_capacity_potential_phs',
    'materials per new res elec capacity installed hvdcs':
    'materials_per_new_res_elec_capacity_installed_hvdcs',
    'materials per new res elec capacity installed material overgrid high power':
    'materials_per_new_res_elec_capacity_installed_material_overgrid_high_power',
    'real growth gtl':
    'real_growth_gtl',
    'scarcity conv gas delayed 1yr':
    'scarcity_conv_gas_delayed_1yr',
    'scarcity conv oil delayed 1yr':
    'scarcity_conv_oil_delayed_1yr',
    'pes natx gas':
    'pes_natx_gas',
    'fe elec generation from unconv gas twh':
    'fe_elec_generation_from_unconv_gas_twh',
    'exponent availability conv oil':
    'exponent_availability_conv_oil',
    'pe losses uncon gas for elec ej':
    'pe_losses_uncon_gas_for_elec_ej',
    'abundance total natx gas':
    'abundance_total_natx_gas',
    'exponent availability conv gas':
    'exponent_availability_conv_gas',
    'scarcity conv gas':
    'scarcity_conv_gas',
    'year scarcity total natx gas':
    'year_scarcity_total_natx_gas',
    'share unconv gas vs tot agg in 2050':
    'share_unconv_gas_vs_tot_agg_in_2050',
    'share unconv gas vs tot agg in 2050 laherrere2010':
    'share_unconv_gas_vs_tot_agg_in_2050_laherrere2010',
    'share unconv gas vs tot agg in 2050 mohr12 bg':
    'share_unconv_gas_vs_tot_agg_in_2050_mohr12_bg',
    'share unconv gas vs tot agg in 2050 user defined':
    'share_unconv_gas_vs_tot_agg_in_2050_user_defined',
    'cumulated tot agg gas extraction to 1995':
    'cumulated_tot_agg_gas_extraction_to_1995',
    'share conv gas vs tot agg':
    'share_conv_gas_vs_tot_agg',
    'share rurr tot agg gas to leave underground':
    'share_rurr_tot_agg_gas_to_leave_underground',
    'rurr tot agg gas':
    'rurr_tot_agg_gas',
    'flow tot agg gas left in ground':
    'flow_tot_agg_gas_left_in_ground',
    'tot rurr tot agg gas':
    'tot_rurr_tot_agg_gas',
    'urr total agg gas unlimited':
    'urr_total_agg_gas_unlimited',
    'start policy leave in ground tot agg gas':
    'start_policy_leave_in_ground_tot_agg_gas',
    'extraction unconv gas tot agg':
    'extraction_unconv_gas_tot_agg',
    'total agg gas left in ground':
    'total_agg_gas_left_in_ground',
    'evolution share unconv gas vs tot agg':
    'evolution_share_unconv_gas_vs_tot_agg',
    'real extraction conv gas ej':
    'real_extraction_conv_gas_ej',
    'urr tot agg gas':
    'urr_tot_agg_gas',
    'cumulated tot agg gas extraction':
    'cumulated_tot_agg_gas_extraction',
    'extraction conv gas tot agg':
    'extraction_conv_gas_tot_agg',
    'real extraction unconv gas ej':
    'real_extraction_unconv_gas_ej',
    'extraction tot agg gas ej':
    'extraction_tot_agg_gas_ej',
    'real extraction conv oil mb div d':
    'real_extraction_conv_oil_mb_div_d',
    'evolution share unconv oil vs tot agg':
    'evolution_share_unconv_oil_vs_tot_agg',
    'share unconv oil vs tot agg in 2050':
    'share_unconv_oil_vs_tot_agg_in_2050',
    'share unconv oil vs tot agg in 2050 laherrere2006':
    'share_unconv_oil_vs_tot_agg_in_2050_laherrere2006',
    'share unconv oil vs tot agg in 2050 user defined':
    'share_unconv_oil_vs_tot_agg_in_2050_user_defined',
    'extraction conv oil tot agg':
    'extraction_conv_oil_tot_agg',
    'extraction unconv oil tot agg':
    'extraction_unconv_oil_tot_agg',
    'share conv oil vs tot agg':
    'share_conv_oil_vs_tot_agg',
    'rurr tot agg oil':
    'rurr_tot_agg_oil',
    'pes oil ej':
    'pes_oil_ej',
    'extraction tot agg oil ej':
    'extraction_tot_agg_oil_ej',
    'real extraction conv oil ej':
    'real_extraction_conv_oil_ej',
    'gch4 per mj conv gas':
    'gch4_per_mj_conv_gas',
    'total agg oil left in ground':
    'total_agg_oil_left_in_ground',
    'cumulated tot agg oil extraction':
    'cumulated_tot_agg_oil_extraction',
    'cumulated tot agg extraction to 1995':
    'cumulated_tot_agg_extraction_to_1995',
    'urr tot agg oil':
    'urr_tot_agg_oil',
    'urr tot agg oil unlimited':
    'urr_tot_agg_oil_unlimited',
    'tot rurr tot agg oil':
    'tot_rurr_tot_agg_oil',
    'start policy leave in ground tot agg oil':
    'start_policy_leave_in_ground_tot_agg_oil',
    'flow tot agg oil left in ground':
    'flow_tot_agg_oil_left_in_ground',
    'g per mt':
    'g_per_mt',
    'share rurr tot agg oil to leave underground':
    'share_rurr_tot_agg_oil_to_leave_underground',
    'gch4 per mj unconv gas':
    'gch4_per_mj_unconv_gas',
    'tot rurr unconv gas':
    'tot_rurr_unconv_gas',
    'start policy leave in ground coal':
    'start_policy_leave_in_ground_coal',
    'total unconv gas left in ground':
    'total_unconv_gas_left_in_ground',
    'flow coal left in ground':
    'flow_coal_left_in_ground',
    'flow conv gas left in ground':
    'flow_conv_gas_left_in_ground',
    'flow conv oil left in ground':
    'flow_conv_oil_left_in_ground',
    'flow unconv oil left in ground':
    'flow_unconv_oil_left_in_ground',
    'share rurr unconv gas to leave underground':
    'share_rurr_unconv_gas_to_leave_underground',
    'share rurr unconv oil to leave underground':
    'share_rurr_unconv_oil_to_leave_underground',
    'tot rurr coal':
    'tot_rurr_coal',
    'tot rurr conv gas':
    'tot_rurr_conv_gas',
    'tot rurr conv oil':
    'tot_rurr_conv_oil',
    'share rurr conv oil to leave underground':
    'share_rurr_conv_oil_to_leave_underground',
    'tot rurr unconv oil':
    'tot_rurr_unconv_oil',
    'total unconv oil left in ground':
    'total_unconv_oil_left_in_ground',
    'total coal left in ground':
    'total_coal_left_in_ground',
    'total conv gas left in ground':
    'total_conv_gas_left_in_ground',
    'total conv oil left in ground':
    'total_conv_oil_left_in_ground',
    'extraction conv oil ej':
    'extraction_conv_oil_ej',
    'extraction coal ej':
    'extraction_coal_ej',
    'rurr coal':
    'rurr_coal',
    'start policy leave in ground unconv gas':
    'start_policy_leave_in_ground_unconv_gas',
    'flow unconv gas left in ground':
    'flow_unconv_gas_left_in_ground',
    'start policy leave in ground unconv oil':
    'start_policy_leave_in_ground_unconv_oil',
    'start policy leave in ground conv oil':
    'start_policy_leave_in_ground_conv_oil',
    'share rurr coal to leave underground':
    'share_rurr_coal_to_leave_underground',
    'pes oil mb div d':
    'pes_oil_mb_div_d',
    'current mineral reserves mt':
    'current_mineral_reserves_mt',
    'share rurr conv gas to leave underground':
    'share_rurr_conv_gas_to_leave_underground',
    'start policy leave in ground conv gas':
    'start_policy_leave_in_ground_conv_gas',
    'extraction conv gas ej':
    'extraction_conv_gas_ej',
    'check gases':
    'check_gases',
    'abundance gases':
    'abundance_gases',
    'demand conv gas':
    'demand_conv_gas',
    'ped natx gas without gtl':
    'ped_natx_gas_without_gtl',
    'abundance solids':
    'abundance_solids',
    'gdp':
    'gdp',
    'fe demand coal elec plants twh':
    'fe_demand_coal_elec_plants_twh',
    'fe demand gas elec plants twh':
    'fe_demand_gas_elec_plants_twh',
    'fed heat gas plus coal ej':
    'fed_heat_gas_plus_coal_ej',
    'pe demand oil elec plants ej':
    'pe_demand_oil_elec_plants_ej',
    'fe demand oil elec plants twh':
    'fe_demand_oil_elec_plants_twh',
    'share coal for elec':
    'share_coal_for_elec',
    'current mineral resources mt':
    'current_mineral_resources_mt',
    'share coalxcoal plus gasx for heat plants':
    'share_coalxcoal_plus_gasx_for_heat_plants',
    'output elec over lifetime res elec for allocation2':
    'output_elec_over_lifetime_res_elec_for_allocation2',
    'demand storage capacity':
    'demand_storage_capacity',
    'share capacity storage div res elec var':
    'share_capacity_storage_div_res_elec_var',
    'static div dynamic quality of electricity quest':
    'static_div_dynamic_quality_of_electricity_quest',
    'xstaticx eroigrid tot effective for allocation res elec':
    'xstaticx_eroigrid_tot_effective_for_allocation_res_elec',
    'ratio eroigrid vs eroi xstaticx':
    'ratio_eroigrid_vs_eroi_xstaticx',
    'ratio eroi per techn vs eroitot xstaticx':
    'ratio_eroi_per_techn_vs_eroitot_xstaticx',
    'total installed capacity res elec var':
    'total_installed_capacity_res_elec_var',
    'share res elec generation curtailed and stored':
    'share_res_elec_generation_curtailed_and_stored',
    'rt storage efficiency phs':
    'rt_storage_efficiency_phs',
    'cp baseload reduction':
    'cp_baseload_reduction',
    'ratio equal x1':
    'ratio_equal_x1',
    'fei over lifetime res elec':
    'fei_over_lifetime_res_elec',
    'real cp res elec':
    'real_cp_res_elec',
    'fei over lifetime res elec for allocation':
    'fei_over_lifetime_res_elec_for_allocation',
    'remaining potential res elec after intermitt':
    'remaining_potential_res_elec_after_intermitt',
    'remaining potential res elec switch':
    'remaining_potential_res_elec_switch',
    'output elec over lifetime res elec for allocation':
    'output_elec_over_lifetime_res_elec_for_allocation',
    'potential res elec after intermitt twh':
    'potential_res_elec_after_intermitt_twh',
    'replacement rate res elec':
    'replacement_rate_res_elec',
    'xstaticx eroitot res elec':
    'xstaticx_eroitot_res_elec',
    'xstaticx eroitot effective for allocation res elec':
    'xstaticx_eroitot_effective_for_allocation_res_elec',
    'new capacity installed onshore wind tw':
    'new_capacity_installed_onshore_wind_tw',
    'ced o and m over lifetime per water res elec var':
    'ced_o_and_m_over_lifetime_per_water_res_elec_var',
    'self electricity consumption res elec':
    'self_electricity_consumption_res_elec',
    'share energy requirements for decom res elec':
    'share_energy_requirements_for_decom_res_elec',
    'ced o and m over lifetime res elec var':
    'ced_o_and_m_over_lifetime_res_elec_var',
    'grid correction factor res elec':
    'grid_correction_factor_res_elec',
    'materials for o and m per capacity installed csp':
    'materials_for_o_and_m_per_capacity_installed_csp',
    'total water for o and m required by res elec per techn':
    'total_water_for_o_and_m_required_by_res_elec_per_techn',
    'water for o and m required for res elec':
    'water_for_o_and_m_required_for_res_elec',
    'materials for o and m per capacity installed res elec':
    'materials_for_o_and_m_per_capacity_installed_res_elec',
    'total energy requirements o and m for water consumption res elec':
    'total_energy_requirements_o_and_m_for_water_consumption_res_elec',
    'energy requirements for o and m for water consumption res elec':
    'energy_requirements_for_o_and_m_for_water_consumption_res_elec',
    'water for o and m res elec':
    'water_for_o_and_m_res_elec',
    'energy requirements per unit of water consumption':
    'energy_requirements_per_unit_of_water_consumption',
    'unlimited nre quest':
    'unlimited_nre_quest',
    'extraction uranium ej':
    'extraction_uranium_ej',
    'urr uranium':
    'urr_uranium',
    'urr conv oil':
    'urr_conv_oil',
    'growth biogas':
    'growth_biogas',
    'past biogas growth':
    'past_biogas_growth',
    'pes biogas ej':
    'pes_biogas_ej',
    'biogas evol':
    'biogas_evol',
    'max biogas ej':
    'max_biogas_ej',
    'fei over lifetime res elec dispatch':
    'fei_over_lifetime_res_elec_dispatch',
    'activate eroi allocation rule':
    'activate_eroi_allocation_rule',
    'eroi allocation rule per res elec':
    'eroi_allocation_rule_per_res_elec',
    'xdynamicx eroi res elec var':
    'xdynamicx_eroi_res_elec_var',
    'eroi ini res elec dispatch':
    'eroi_ini_res_elec_dispatch',
    'activate exogenous res elec cp reduction quest':
    'activate_exogenous_res_elec_cp_reduction_quest',
    'res elec capacity under construction tw':
    'res_elec_capacity_under_construction_tw',
    'real generation solar pv ej':
    'real_generation_solar_pv_ej',
    'materials required for new csp mt':
    'materials_required_for_new_csp_mt',
    'materials required for new pv mt':
    'materials_required_for_new_pv_mt',
    'materials required for new wind offshore mt':
    'materials_required_for_new_wind_offshore_mt',
    'materials required for new wind onshore mt':
    'materials_required_for_new_wind_onshore_mt',
    'materials required for o and m csp mt':
    'materials_required_for_o_and_m_csp_mt',
    'materials required for o and m pv mt':
    'materials_required_for_o_and_m_pv_mt',
    'materials required for o and m wind offshore mt':
    'materials_required_for_o_and_m_wind_offshore_mt',
    'materials required for o and m wind onshore mt':
    'materials_required_for_o_and_m_wind_onshore_mt',
    'real generation res elec ej':
    'real_generation_res_elec_ej',
    'cedtot solar pv':
    'cedtot_solar_pv',
    'total materials required for new res elec mt':
    'total_materials_required_for_new_res_elec_mt',
    'total materials required for o and m res elec mt':
    'total_materials_required_for_o_and_m_res_elec_mt',
    'eroi equal x1':
    'eroi_equal_x1',
    'electrical distribution losses twh':
    'electrical_distribution_losses_twh',
    'max share transm and distr elec losses':
    'max_share_transm_and_distr_elec_losses',
    'heat com distribution losses':
    'heat_com_distribution_losses',
    'potential generation res elec twh':
    'potential_generation_res_elec_twh',
    'output elec over lifetime res elec':
    'output_elec_over_lifetime_res_elec',
    'variation share transm and distr elec losses':
    'variation_share_transm_and_distr_elec_losses',
    'remaining share transm and distr elec losses':
    'remaining_share_transm_and_distr_elec_losses',
    'share transm and distr elec losses':
    'share_transm_and_distr_elec_losses',
    'total gen losses demand for elec plants ej':
    'total_gen_losses_demand_for_elec_plants_ej',
    'pe losses bioe for elec ej':
    'pe_losses_bioe_for_elec_ej',
    'water for o and m wind offshore':
    'water_for_o_and_m_wind_offshore',
    'total materials required for res elec mt':
    'total_materials_required_for_res_elec_mt',
    'share energy for material consumption for alt techn vs tfec':
    'share_energy_for_material_consumption_for_alt_techn_vs_tfec',
    'water for o and m pv':
    'water_for_o_and_m_pv',
    'water for o and m wind onshore':
    'water_for_o_and_m_wind_onshore',
    'materials for o and m per capacity installed wind offshore':
    'materials_for_o_and_m_per_capacity_installed_wind_offshore',
    'materials for o and m per capacity installed wind onshore':
    'materials_for_o_and_m_per_capacity_installed_wind_onshore',
    'materials for o and m per capacity installed pv':
    'materials_for_o_and_m_per_capacity_installed_pv',
    'water for o and m csp':
    'water_for_o_and_m_csp',
    'materials per capacity installed pv x0':
    'materials_per_capacity_installed_pv_x0',
    'cum materials requirements for res elec':
    'cum_materials_requirements_for_res_elec',
    'mj per ej':
    'mj_per_ej',
    'initial energy cons per unit of material cons xvirginx':
    'initial_energy_cons_per_unit_of_material_cons_xvirginx',
    'materials per new capacity installed csp':
    'materials_per_new_capacity_installed_csp',
    'materials per new capacity installed wind offshore':
    'materials_per_new_capacity_installed_wind_offshore',
    'materials per new capacity installed wind onshore':
    'materials_per_new_capacity_installed_wind_onshore',
    'initial cumulated material requirements for res elec 1995':
    'initial_cumulated_material_requirements_for_res_elec_1995',
    'materials per new capacity installed pv':
    'materials_per_new_capacity_installed_pv',
    'kg per mt':
    'kg_per_mt',
    'm per t':
    'm_per_t',
    'elec generation variable from res twh':
    'elec_generation_variable_from_res_twh',
    'new required capacity nuclear':
    'new_required_capacity_nuclear',
    'replacement res for heat com':
    'replacement_res_for_heat_com',
    'losses solar for heat':
    'losses_solar_for_heat',
    'cp ini res for heat':
    'cp_ini_res_for_heat',
    'cp ini res elec sub hydro':
    'cp_ini_res_elec_sub_hydro',
    'efficiency geothermal for heat':
    'efficiency_geothermal_for_heat',
    'efficiency solar panels for heat':
    'efficiency_solar_panels_for_heat',
    'max fe potential res for heat':
    'max_fe_potential_res_for_heat',
    'p geothermal for heat':
    'p_geothermal_for_heat',
    'past res growth for heat com':
    'past_res_growth_for_heat_com',
    'installed capacity res heat com tw':
    'installed_capacity_res_heat_com_tw',
    'initial value res for heat com':
    'initial_value_res_for_heat_com',
    'p solar for heat':
    'p_solar_for_heat',
    'life time res for heat':
    'life_time_res_for_heat',
    'wear res capacity for heat com tw':
    'wear_res_capacity_for_heat_com_tw',
    'potential fe gen elec fossil fuel chp plants ej':
    'potential_fe_gen_elec_fossil_fuel_chp_plants_ej',
    'fed heat liquids chp plants ej':
    'fed_heat_liquids_chp_plants_ej',
    'fed heat coal chp plants ej':
    'fed_heat_coal_chp_plants_ej',
    'remaining potential csp':
    'remaining_potential_csp',
    'pe csp for elec generation ej':
    'pe_csp_for_elec_generation_ej',
    'invest res for elec':
    'invest_res_for_elec',
    'power density csp':
    'power_density_csp',
    'max potential res elec twe':
    'max_potential_res_elec_twe',
    'surface csp mha':
    'surface_csp_mha',
    'fe elec generation from csp twh':
    'fe_elec_generation_from_csp_twh',
    'invest csp tdolar':
    'invest_csp_tdolar',
    'cp limit nuclear':
    'cp_limit_nuclear',
    'cp nuclear':
    'cp_nuclear',
    'installed capacity nuclear tw':
    'installed_capacity_nuclear_tw',
    'nuclear capacity phase out':
    'nuclear_capacity_phase_out',
    'min cp nuclear':
    'min_cp_nuclear',
    'replacement nuclear capacity':
    'replacement_nuclear_capacity',
    'min cp baseload res':
    'min_cp_baseload_res',
    'abundance uranium':
    'abundance_uranium',
    'nuclear overcapacity':
    'nuclear_overcapacity',
    'p nuclear scen3x x4':
    'p_nuclear_scen3x_x4',
    'start year nuclear growth scen3x x4':
    'start_year_nuclear_growth_scen3x_x4',
    'p nuclear elec gen':
    'p_nuclear_elec_gen',
    'required capacity nuclear tw':
    'required_capacity_nuclear_tw',
    'time planification nuclear':
    'time_planification_nuclear',
    'time construction nuclear':
    'time_construction_nuclear',
    'initial capacity installed nuclear':
    'initial_capacity_installed_nuclear',
    'new nuclear capacity under planning':
    'new_nuclear_capacity_under_planning',
    'selection of nuclear scenario':
    'selection_of_nuclear_scenario',
    'initial gen nuclear':
    'initial_gen_nuclear',
    'initial capacity in construction nuclear':
    'initial_capacity_in_construction_nuclear',
    'initial required capacity nuclear':
    'initial_required_capacity_nuclear',
    'planned nuclear capacity tw':
    'planned_nuclear_capacity_tw',
    'wear nuclear':
    'wear_nuclear',
    'effects shortage uranium':
    'effects_shortage_uranium',
    'tpes intensity ej tdollar':
    'tpes_intensity_ej_tdollar',
    'real ped intensity of electricity':
    'real_ped_intensity_of_electricity',
    'annual gdp growth rate':
    'annual_gdp_growth_rate',
    'gdp delayed 1yr':
    'gdp_delayed_1yr',
    'share tot monet invest elec res vs gdp':
    'share_tot_monet_invest_elec_res_vs_gdp',
    'gdppc':
    'gdppc',
    'unlimited coal quest':
    'unlimited_coal_quest',
    'real tfec':
    'real_tfec',
    'unlimited uranium quest':
    'unlimited_uranium_quest',
    'urr coal unlimited':
    'urr_coal_unlimited',
    'urr uranium unlimited':
    'urr_uranium_unlimited',
    'urr conv gas unlimited':
    'urr_conv_gas_unlimited',
    'unlimited gas quest':
    'unlimited_gas_quest',
    'unlimited oil quest':
    'unlimited_oil_quest',
    'urr conv oil unlimited':
    'urr_conv_oil_unlimited',
    'b logistic':
    'b_logistic',
    'a logistic':
    'a_logistic',
    'activate elf by scen quest':
    'activate_elf_by_scen_quest',
    'total demand liquids mb div d':
    'total_demand_liquids_mb_div_d',
    'ped coal without ctl':
    'ped_coal_without_ctl',
    'surface hydro mha':
    'surface_hydro_mha',
    'remaining potential hydro':
    'remaining_potential_hydro',
    'grid reinforcement costs tdollar':
    'grid_reinforcement_costs_tdollar',
    'remaining potential onshore wind':
    'remaining_potential_onshore_wind',
    'remaining potential offshore wind':
    'remaining_potential_offshore_wind',
    'remaining potential bioe':
    'remaining_potential_bioe',
    'remaining potential oceanic':
    'remaining_potential_oceanic',
    'remaining potential geot elec':
    'remaining_potential_geot_elec',
    'remaining potential solar elec pv':
    'remaining_potential_solar_elec_pv',
    'initial non energy use':
    'initial_non_energy_use',
    'real total output':
    'real_total_output',
    'real demand':
    'real_demand',
    'max potential res elec twh':
    'max_potential_res_elec_twh',
    'pe onshore wind for elec generation ej':
    'pe_onshore_wind_for_elec_generation_ej',
    'fe elec generation from solar pv twh':
    'fe_elec_generation_from_solar_pv_twh',
    'power density solar pv':
    'power_density_solar_pv',
    'pe hydro for elec generation ej':
    'pe_hydro_for_elec_generation_ej',
    'invest biow tdolar':
    'invest_biow_tdolar',
    'fe elec generation from hydro twh':
    'fe_elec_generation_from_hydro_twh',
    'invest geot elec tdolar':
    'invest_geot_elec_tdolar',
    'invest hydro tdolar':
    'invest_hydro_tdolar',
    'fe elec generation from onshore wind twh':
    'fe_elec_generation_from_onshore_wind_twh',
    'invest oceanic tdolar':
    'invest_oceanic_tdolar',
    'invest onshore wind tdolar':
    'invest_onshore_wind_tdolar',
    'invest offshore wind tdolar':
    'invest_offshore_wind_tdolar',
    'fe elec generation from geot elec twh':
    'fe_elec_generation_from_geot_elec_twh',
    'pe geot elec for elec generation ej':
    'pe_geot_elec_for_elec_generation_ej',
    'pe solar pv for elec generation ej':
    'pe_solar_pv_for_elec_generation_ej',
    'fe elec generation from bioe twh':
    'fe_elec_generation_from_bioe_twh',
    'pe oceanic for elec generation ej':
    'pe_oceanic_for_elec_generation_ej',
    'pe bioe for elec generation ej':
    'pe_bioe_for_elec_generation_ej',
    'fe elec generation from offshore wind twh':
    'fe_elec_generation_from_offshore_wind_twh',
    'fe elec generation from oceanic twh':
    'fe_elec_generation_from_oceanic_twh',
    'pe offshore wind for elec generation ej':
    'pe_offshore_wind_for_elec_generation_ej',
    'invest solar tdolar':
    'invest_solar_tdolar',
    'initial value land compet biofuels 2gen mha':
    'initial_value_land_compet_biofuels_2gen_mha',
    'initial value land compet biofuels 2gen ktoe':
    'initial_value_land_compet_biofuels_2gen_ktoe',
    'abundance coal':
    'abundance_coal',
    'abundance liquids':
    'abundance_liquids',
    'check liquids':
    'check_liquids',
    'share heat distribution losses':
    'share_heat_distribution_losses',
    'potential tot res elec after intermitt':
    'potential_tot_res_elec_after_intermitt',
    'pe biow for elec generation mtoe':
    'pe_biow_for_elec_generation_mtoe',
    'remaining potential tot res elec after intermitt':
    'remaining_potential_tot_res_elec_after_intermitt',
    'power density res elec twe div mha':
    'power_density_res_elec_twe_div_mha',
    'power density res elec tw div mha':
    'power_density_res_elec_tw_div_mha',
    'time 95pc ts potential res elec':
    'time_95pc_ts_potential_res_elec',
    'surface res elec':
    'surface_res_elec',
    'max geot elec twe':
    'max_geot_elec_twe',
    'max pe geot elec twth':
    'max_pe_geot_elec_twth',
    'efficiency conversion geot pe to elec':
    'efficiency_conversion_geot_pe_to_elec',
    'geot pe potential for heat ej':
    'geot_pe_potential_for_heat_ej',
    'initial instal cap res elec':
    'initial_instal_cap_res_elec',
    'abundance res elec2':
    'abundance_res_elec2',
    'potential tot generation res elec twh':
    'potential_tot_generation_res_elec_twh',
    'res elec tot overcapacity':
    'res_elec_tot_overcapacity',
    'wear res elec':
    'wear_res_elec',
    'cp ini res elec':
    'cp_ini_res_elec',
    'g per t':
    'g_per_t',
    'time construction res elec':
    'time_construction_res_elec',
    'time planification res elec':
    'time_planification_res_elec',
    'new res elec capacity under planning':
    'new_res_elec_capacity_under_planning',
    'lifetime res elec':
    'lifetime_res_elec',
    'past res elec capacity growth':
    'past_res_elec_capacity_growth',
    'mt per gt':
    'mt_per_gt',
    'gtl efficiency':
    'gtl_efficiency',
    'ctl efficiency':
    'ctl_efficiency',
    'ctl plus gtl gb':
    'ctl_plus_gtl_gb',
    'mb div d per ej div year':
    'mb_div_d_per_ej_div_year',
    'hist growth ctl':
    'hist_growth_ctl',
    'gboe per ej':
    'gboe_per_ej',
    'hist growth gtl':
    'hist_growth_gtl',
    'urr uranium user defined':
    'urr_uranium_user_defined',
    'replacement rate nuclear':
    'replacement_rate_nuclear',
    'demand gas for oil refinery gains':
    'demand_gas_for_oil_refinery_gains',
    'share res vs tpes':
    'share_res_vs_tpes',
    'tpes mtoe':
    'tpes_mtoe',
    'fe elec generation from nre twh':
    'fe_elec_generation_from_nre_twh',
    'pepc consumption people depending on trad biomass':
    'pepc_consumption_people_depending_on_trad_biomass',
    'share gas for oil refinery gains':
    'share_gas_for_oil_refinery_gains',
    'people relying trad biomass ref':
    'people_relying_trad_biomass_ref',
    'pe consumption trad biomass ref':
    'pe_consumption_trad_biomass_ref',
    'tpefpc threshold high development':
    'tpefpc_threshold_high_development',
    'tped acceptable standard living':
    'tped_acceptable_standard_living',
    'pop not dependent on trad biomass':
    'pop_not_dependent_on_trad_biomass',
    'carbon footprint tco2x div person':
    'carbon_footprint_tco2x_div_person',
    'average tpespc xwithout trad biomassx':
    'average_tpespc_xwithout_trad_biomassx',
    'tpes xwithout trad biomassx':
    'tpes_xwithout_trad_biomassx',
    'max npp potential bioe residues for heat and elec':
    'max_npp_potential_bioe_residues_for_heat_and_elec',
    'max npp potential bioe residues for cellulosic biofuels':
    'max_npp_potential_bioe_residues_for_cellulosic_biofuels',
    'total cumulative emissions gtco2':
    'total_cumulative_emissions_gtco2',
    'carbon emissions gtc':
    'carbon_emissions_gtc',
    'gco2 per mj unconv gas':
    'gco2_per_mj_unconv_gas',
    'gco2 per mj unconv oil':
    'gco2_per_mj_unconv_oil',
    'co2 emissions ctl':
    'co2_emissions_ctl',
    'gco2 per mj conv gas':
    'gco2_per_mj_conv_gas',
    'gco2 per mj ctl':
    'gco2_per_mj_ctl',
    'gco2 per mj gtl':
    'gco2_per_mj_gtl',
    'gco2 per mj coal':
    'gco2_per_mj_coal',
    'gco2 per mj conv oil':
    'gco2_per_mj_conv_oil',
    'gco2 per mj shale oil':
    'gco2_per_mj_shale_oil',
    'dollars to tdollars':
    'dollars_to_tdollars',
    'land compet 2gen vs total land compet':
    'land_compet_2gen_vs_total_land_compet',
    'gj per ej':
    'gj_per_ej',
    'land shifted to biofuels 3gen':
    'land_shifted_to_biofuels_3gen',
    'average tpes per capita':
    'average_tpes_per_capita',
    'geot pe potential for heat twth':
    'geot_pe_potential_for_heat_twth',
    'pe losses uranium for elec ej':
    'pe_losses_uranium_for_elec_ej',
    'share res for elec vs tpe res':
    'share_res_for_elec_vs_tpe_res',
    'extraction coal mtoe':
    'extraction_coal_mtoe',
    'max extraction coal mtoe':
    'max_extraction_coal_mtoe',
    'tpe from res ej':
    'tpe_from_res_ej',
    'tpe from res mtoe':
    'tpe_from_res_mtoe',
    'electrical distribution losses ej':
    'electrical_distribution_losses_ej',
    'efficiency conversion bioe plants to heat':
    'efficiency_conversion_bioe_plants_to_heat',
    'efficiency improvement biofuels 3gen':
    'efficiency_improvement_biofuels_3gen',
    'potential peavail biofuels 2gen land compet ej':
    'potential_peavail_biofuels_2gen_land_compet_ej',
    'annual additional historic land use biofuels 2gen':
    'annual_additional_historic_land_use_biofuels_2gen',
    'max npp potential bioe residues':
    'max_npp_potential_bioe_residues',
    'grid reinforcement costs':
    'grid_reinforcement_costs',
    'historic land compet available for biofuels 2gen':
    'historic_land_compet_available_for_biofuels_2gen',
    'land productivity biofuels 2gen ej mha':
    'land_productivity_biofuels_2gen_ej_mha',
    'max peavail potential biofuels 2 x3gen':
    'max_peavail_potential_biofuels_2_x3gen',
    'land compet biofuels 2gen mha':
    'land_compet_biofuels_2gen_mha',
    'efficiency conversion bioe to elec':
    'efficiency_conversion_bioe_to_elec',
    'potential peavail biofuels prod 3gen ej':
    'potential_peavail_biofuels_prod_3gen_ej',
    'max peavail potential bioe residues for cellulosic biofuels':
    'max_peavail_potential_bioe_residues_for_cellulosic_biofuels',
    'p biofuels 3gen':
    'p_biofuels_3gen',
    'constrain gas exogenous growth quest delayed x1yr':
    'constrain_gas_exogenous_growth_quest_delayed_x1yr',
    'constrain gas exogenous growth quest':
    'constrain_gas_exogenous_growth_quest',
    'constrain liquids exogenous growth quest delayed x1yr':
    'constrain_liquids_exogenous_growth_quest_delayed_x1yr',
    'check liquids delayed 1yr':
    'check_liquids_delayed_1yr',
    'check gas delayed 1yr':
    'check_gas_delayed_1yr',
    'constrain liquids exogenous growth quest':
    'constrain_liquids_exogenous_growth_quest',
    'share variable res elec vs total generation delayed 1yr':
    'share_variable_res_elec_vs_total_generation_delayed_1yr',
    'overcapacity vsx intermittent res penetration x0':
    'overcapacity_vsx_intermittent_res_penetration_x0',
    'total electrical losses ej':
    'total_electrical_losses_ej',
    'gen losses vs pe for elec':
    'gen_losses_vs_pe_for_elec',
    'initial gtl production':
    'initial_gtl_production',
    'initial ctl production':
    'initial_ctl_production',
    'pe demand gas elec plants ej':
    'pe_demand_gas_elec_plants_ej',
    'pe demand coal elec plants ej':
    'pe_demand_coal_elec_plants_ej',
    'max efficiency gas power plants':
    'max_efficiency_gas_power_plants',
    'total pe for electricity consumption ej':
    'total_pe_for_electricity_consumption_ej',
    'initial efficiency gas for electricity':
    'initial_efficiency_gas_for_electricity',
    'remaining efficiency improv gas for electricity':
    'remaining_efficiency_improv_gas_for_electricity',
    'efficiency improv gas for electricity':
    'efficiency_improv_gas_for_electricity',
    'efficiency gas for electricity':
    'efficiency_gas_for_electricity',
    'percent to share':
    'percent_to_share',
    'additional pe production of ctl plus gtl for liquids':
    'additional_pe_production_of_ctl_plus_gtl_for_liquids',
    'carbon budget':
    'carbon_budget',
    'cumulative emissions to 1995':
    'cumulative_emissions_to_1995',
    'fe solar potential for heat':
    'fe_solar_potential_for_heat',
    'start year bioe residues for heat plus elec':
    'start_year_bioe_residues_for_heat_plus_elec',
    'co2 fossil fuel emissions':
    'co2_fossil_fuel_emissions',
    't per gt':
    't_per_gt',
    'share land compet biofuels':
    'share_land_compet_biofuels',
    'share land total res vs arable':
    'share_land_total_res_vs_arable',
    'share land res land compet vs arable':
    'share_land_res_land_compet_vs_arable',
    'year scarcity oil':
    'year_scarcity_oil',
    'cumulated conv gas extraction':
    'cumulated_conv_gas_extraction',
    'cumulated conv gas extraction to 1995':
    'cumulated_conv_gas_extraction_to_1995',
    'cumulated unconv gas extraction':
    'cumulated_unconv_gas_extraction',
    'cumulated unconv gas extraction to 1995':
    'cumulated_unconv_gas_extraction_to_1995',
    'rurr uranium':
    'rurr_uranium',
    'cumulated uranium extraction to 1995':
    'cumulated_uranium_extraction_to_1995',
    'cumulated conv oil extraction':
    'cumulated_conv_oil_extraction',
    'cumulated conv oil extraction to 1995':
    'cumulated_conv_oil_extraction_to_1995',
    'cumulated unconv oil extraction':
    'cumulated_unconv_oil_extraction',
    'cumulated coal extraction':
    'cumulated_coal_extraction',
    'cumulated coal extraction to 1995':
    'cumulated_coal_extraction_to_1995',
    'cumulated unconv oil extraction to 1995':
    'cumulated_unconv_oil_extraction_to_1995',
    'cumulated uranium extraction':
    'cumulated_uranium_extraction',
    'oil refinery gains ej':
    'oil_refinery_gains_ej',
    'oil refinery gains share':
    'oil_refinery_gains_share',
    'efficiency gas for oil refinery gains':
    'efficiency_gas_for_oil_refinery_gains',
    'pes liquids ej':
    'pes_liquids_ej',
    'one year':
    'one_year',
    'land compet required dedicated crops for biofuels':
    'land_compet_required_dedicated_crops_for_biofuels',
    'new biofuels 2gen land compet':
    'new_biofuels_2gen_land_compet',
    'annual shift from 2gen to 3gen':
    'annual_shift_from_2gen_to_3gen',
    'land compet biofuels 3gen mha':
    'land_compet_biofuels_3gen_mha',
    'p bioe residues for heat plus elec':
    'p_bioe_residues_for_heat_plus_elec',
    'potential pe cellulosic biofuel ej':
    'potential_pe_cellulosic_biofuel_ej',
    'cellulosic biofuels available':
    'cellulosic_biofuels_available',
    'bioe residues for heat plus elec available':
    'bioe_residues_for_heat_plus_elec_available',
    'pe bioe residues for heat plus elec ej':
    'pe_bioe_residues_for_heat_plus_elec_ej',
    'p cellulosic biofuels':
    'p_cellulosic_biofuels',
    'share cellulosic biofuels vs bioe residues':
    'share_cellulosic_biofuels_vs_bioe_residues',
    'start year cellulosic biofuels':
    'start_year_cellulosic_biofuels',
    'share land total res vs urban surface':
    'share_land_total_res_vs_urban_surface',
    'max land compet biofuels 2gen':
    'max_land_compet_biofuels_2gen',
    'p biofuels 2gen':
    'p_biofuels_2gen',
    'past biofuels 2gen':
    'past_biofuels_2gen',
    'ej per ktoe':
    'ej_per_ktoe',
    'abundance total oil':
    'abundance_total_oil',
    'cp nuclear initial':
    'cp_nuclear_initial',
    'extraction coal without ctl ej':
    'extraction_coal_without_ctl_ej',
    'extraction coal for ctl ej':
    'extraction_coal_for_ctl_ej',
    'other liquids supply ej':
    'other_liquids_supply_ej',
    'max offshore wind twe':
    'max_offshore_wind_twe',
    'urr unconv oil high mohr15':
    'urr_unconv_oil_high_mohr15',
    'urr unconv oil low mohr15':
    'urr_unconv_oil_low_mohr15',
    'urr unconv oil user defined':
    'urr_unconv_oil_user_defined',
    'urr uranium zittel12':
    'urr_uranium_zittel12',
    'urr conv oil maggio12 high':
    'urr_conv_oil_maggio12_high',
    'urr conv oil maggio12 low':
    'urr_conv_oil_maggio12_low',
    'separate conv and unconv gas quest':
    'separate_conv_and_unconv_gas_quest',
    'urr tot agg oil laherrere 2006':
    'urr_tot_agg_oil_laherrere_2006',
    'urr tot agg oil user defined':
    'urr_tot_agg_oil_user_defined',
    'choose extraction curve tot agg oil':
    'choose_extraction_curve_tot_agg_oil',
    'urr conv oil maggio12 middle':
    'urr_conv_oil_maggio12_middle',
    'urr conv oil user defined':
    'urr_conv_oil_user_defined',
    'choose extraction tot agg gas curve':
    'choose_extraction_tot_agg_gas_curve',
    'urr unconv oil bg mohr15':
    'urr_unconv_oil_bg_mohr15',
    'separate conv and unconv oil quest':
    'separate_conv_and_unconv_oil_quest',
    'urr uranium ewg13':
    'urr_uranium_ewg13',
    'kt uranium per ej':
    'kt_uranium_per_ej',
    'life time nuclear':
    'life_time_nuclear',
    'surface solar pv mha':
    'surface_solar_pv_mha',
    'cumulated uranium extraction kt':
    'cumulated_uranium_extraction_kt',
    'extraction uranium kt':
    'extraction_uranium_kt',
    'efficiency uranium for electricity':
    'efficiency_uranium_for_electricity',
    'fe nuclear elec generation twh':
    'fe_nuclear_elec_generation_twh',
    'kwh per twh':
    'kwh_per_twh',
    'total fe elec demand ej':
    'total_fe_elec_demand_ej',
    'gco2e per kwh biomass':
    'gco2e_per_kwh_biomass',
    'mtoe per ej':
    'mtoe_per_ej',
    'share transm and distr elec losses initial':
    'share_transm_and_distr_elec_losses_initial',
    'ej per twh':
    'ej_per_twh',
    'surface onshore wind mha':
    'surface_onshore_wind_mha',
    'twe per twh':
    'twe_per_twh',
    'initial population':
    'initial_population',
    'population':
    'population',
    've objetive ue2020 extrap':
    've_objetive_ue2020_extrap',
    've objetive ue2020':
    've_objetive_ue2020',
    'choose extraction uranium curve':
    'choose_extraction_uranium_curve',
    'year scarcity tpe':
    'year_scarcity_tpe',
    'year scarcity uranium':
    'year_scarcity_uranium',
    'year scarcity coal':
    'year_scarcity_coal',
    'year scarcity liquids':
    'year_scarcity_liquids',
    'effects shortage gas':
    'effects_shortage_gas',
    'year scarcity gases':
    'year_scarcity_gases',
    'max percent of change':
    'max_percent_of_change',
    'choose extraction coal curve':
    'choose_extraction_coal_curve',
    'selection constraint extraction unconv gas':
    'selection_constraint_extraction_unconv_gas',
    'year scarcity elec':
    'year_scarcity_elec',
    'extraction unconv gas delayed':
    'extraction_unconv_gas_delayed',
    'max unconv gas growth extraction ej':
    'max_unconv_gas_growth_extraction_ej',
    'p constraint growth extraction unconv gas':
    'p_constraint_growth_extraction_unconv_gas',
    'choose extraction curve unconv gas':
    'choose_extraction_curve_unconv_gas',
    'choose extraction curve unconv oil':
    'choose_extraction_curve_unconv_oil',
    'biofuels land compet available':
    'biofuels_land_compet_available',
    'urr oil aspo':
    'urr_oil_aspo',
    'urr gas mohr high2013':
    'urr_gas_mohr_high2013',
    'urr gas leherrere2010':
    'urr_gas_leherrere2010',
    'urr gas mohr bg2012':
    'urr_gas_mohr_bg2012',
    'res to fossil accounting':
    'res_to_fossil_accounting',
    'new c gtc':
    'new_c_gtc',
    'year adjust':
    'year_adjust',
    'urban surface 2008':
    'urban_surface_2008',
    'c per co2':
    'c_per_co2',
    'activate affores program':
    'activate_affores_program',
    'global arable land':
    'global_arable_land',
    'choose extraction curve conv oil':
    'choose_extraction_curve_conv_oil',
    'choose extraction conv gas curve':
    'choose_extraction_conv_gas_curve',
    'cumulated total monet invest res for elec':
    'cumulated_total_monet_invest_res_for_elec',
    'efficiency coal for electricity':
    'efficiency_coal_for_electricity',
    'efficiency liquids for electricity':
    'efficiency_liquids_for_electricity',
    'additional land compet available for biofuels':
    'additional_land_compet_available_for_biofuels',
    'max hydro twe':
    'max_hydro_twe',
    'max oceanic twe':
    'max_oceanic_twe',
    'max onshore wind twe':
    'max_onshore_wind_twe',
    'p ctl':
    'p_ctl',
    'p gtl':
    'p_gtl',
    'start year 3gen':
    'start_year_3gen',
    'share variable res elec generation vs total':
    'share_variable_res_elec_generation_vs_total',
    'total cumulative emissions gtc':
    'total_cumulative_emissions_gtc',
    'p nuclear scen 1':
    'p_nuclear_scen_1',
    'p nuclear 2 x3':
    'p_nuclear_2_x3',
    'gco2e per gtco2e 4':
    'gco2e_per_gtco2e_4',
    'gco2e per gtco2e 3':
    'gco2e_per_gtco2e_3',
    'gco2e per gtco2e 0':
    'gco2e_per_gtco2e_0',
    'gco2e per gtco2e 1':
    'gco2e_per_gtco2e_1',
    'twh per gco2e 0':
    'twh_per_gco2e_0',
    'fed heat coal plants ej':
    'fed_heat_coal_plants_ej',
    'fed heat com ej':
    'fed_heat_com_ej',
    'total fe elec demand twh':
    'total_fe_elec_demand_twh',
    'real demand by sector':
    'real_demand_by_sector',
    'required total output by sector':
    'required_total_output_by_sector',
    'rurr unconv oil ej':
    'rurr_unconv_oil_ej',
    'share liquids for final energy':
    'share_liquids_for_final_energy',
    'ped liquids ej':
    'ped_liquids_ej',
    'fed heat liquids plants ej':
    'fed_heat_liquids_plants_ej',
    'real final energy by sector and fuel':
    'real_final_energy_by_sector_and_fuel',
    'hist var inlandt':
    'hist_var_inlandt',
    'inland transport variation intensity':
    'inland_transport_variation_intensity',
    'fed heat com nre ej':
    'fed_heat_com_nre_ej',
    'real fe consumption by fuel':
    'real_fe_consumption_by_fuel',
    'other liquids required ej':
    'other_liquids_required_ej',
    'fe elec demand consum ej':
    'fe_elec_demand_consum_ej',
    'required fed by liquids ej':
    'required_fed_by_liquids_ej',
    'real gfcf':
    'real_gfcf',
    'real household demand':
    'real_household_demand',
    'demand conv oil ej':
    'demand_conv_oil_ej',
    'max unconv oil growth extraction ej':
    'max_unconv_oil_growth_extraction_ej',
    'fe demand elec consum twh':
    'fe_demand_elec_consum_twh',
    'total fed heat com ej':
    'total_fed_heat_com_ej',
    'real total output by fuel and sector':
    'real_total_output_by_fuel_and_sector',
    'required final energy by sector and fuel':
    'required_final_energy_by_sector_and_fuel',
    'urr unconv oil':
    'urr_unconv_oil',
    'fed heat gas plants ej':
    'fed_heat_gas_plants_ej',
    'urr coal':
    'urr_coal',
    'urr conv gas':
    'urr_conv_gas',
    'real demand by sector delayed':
    'real_demand_by_sector_delayed',
    'required final energy other transport':
    'required_final_energy_other_transport',
    'real total output by sector':
    'real_total_output_by_sector',
    'required final energy air transport':
    'required_final_energy_air_transport',
    'required final energy inland transport':
    'required_final_energy_inland_transport',
    'required final energy water transport':
    'required_final_energy_water_transport',
    'urr coal bg mohr15':
    'urr_coal_bg_mohr15',
    'urr coal user defined ej':
    'urr_coal_user_defined_ej',
    'urr conv gas bg mohr15':
    'urr_conv_gas_bg_mohr15',
    'urr conv gas high mohr15':
    'urr_conv_gas_high_mohr15',
    'urr conv gas low mohr15':
    'urr_conv_gas_low_mohr15',
    'urr conv gas user defined':
    'urr_conv_gas_user_defined',
    'urr total gas laherrere10':
    'urr_total_gas_laherrere10',
    'urr total gas mohr12 bg':
    'urr_total_gas_mohr12_bg',
    'urr total gas user defined':
    'urr_total_gas_user_defined',
    'urr unconv gas':
    'urr_unconv_gas',
    'urr unconv gas bg mohr15':
    'urr_unconv_gas_bg_mohr15',
    'urr unconv gas low mohr15':
    'urr_unconv_gas_low_mohr15',
    'urr coal high15':
    'urr_coal_high15',
    'urr coal low mohr15':
    'urr_coal_low_mohr15',
    'urr unconv gas high mohr15':
    'urr_unconv_gas_high_mohr15',
    'urr unconv gas user defined':
    'urr_unconv_gas_user_defined',
    'urr coal mohr2012 ej':
    'urr_coal_mohr2012_ej',
    'selection constraint extraction unconv oil':
    'selection_constraint_extraction_unconv_oil',
    'abundance electricity':
    'abundance_electricity',
    'p constraint growth extraction unconv oil':
    'p_constraint_growth_extraction_unconv_oil',
    'extraction unconv oil delayed':
    'extraction_unconv_oil_delayed',
    'final time':
    'final_time',
    'initial time':
    'initial_time',
    'saveper':
    'saveper',
    'time step':
    'time_step',
    'historic share e industry own use vs tfec':
    'historic_share_e_industry_own_use_vs_tfec',
    'historic rate final energy intensity':
    'historic_rate_final_energy_intensity',
    'historic rate final energy intensity h':
    'historic_rate_final_energy_intensity_h',
    'share gas div xcoal plus gasx for heat plants':
    'share_gas_div_xcoal_plus_gasx_for_heat_plants',
    'share liquids fot heat plants':
    'share_liquids_fot_heat_plants',
    'share gas div xcoal plus gasx for elec':
    'share_gas_div_xcoal_plus_gasx_for_elec',
    'demand elec gas and coal twh':
    'demand_elec_gas_and_coal_twh',
    'share oil for elec':
    'share_oil_for_elec',
    'new cellulosic biofuels':
    'new_cellulosic_biofuels',
    'new bioe residues for heat plus elec':
    'new_bioe_residues_for_heat_plus_elec',
    'new biofuels land marg':
    'new_biofuels_land_marg',
    'a lineal regr phase out oil for heat':
    'a_lineal_regr_phase_out_oil_for_heat',
    'a lineal regr phase out oil for elec':
    'a_lineal_regr_phase_out_oil_for_elec',
    'co2x soil and luc emissions':
    'co2x_soil_and_luc_emissions',
    'other forcings rcp':
    'other_forcings_rcp',
    'halocarbon rf':
    'halocarbon_rf',
    'other forcings':
    'other_forcings',
    'global ch4 anthro emissions':
    'global_ch4_anthro_emissions',
    'global hfc emissions':
    'global_hfc_emissions',
    'global pfc emissions':
    'global_pfc_emissions',
    'global sf6 emissions':
    'global_sf6_emissions',
    'global n2o anthro emissions':
    'global_n2o_anthro_emissions',
    'historic water by type intensities by sector':
    'historic_water_by_type_intensities_by_sector',
    'historic water by type intensities for households':
    'historic_water_by_type_intensities_for_households',
    'total co2 emissions gtco2':
    'total_co2_emissions_gtco2',
    'adapt growth res for heat 0':
    'adapt_growth_res_for_heat_0',
    'adapt growth res for heat com':
    'adapt_growth_res_for_heat_com',
    'adapt growth res for heat nc':
    'adapt_growth_res_for_heat_nc',
    'adapt growth waste':
    'adapt_growth_waste',
    'adapt growth biogas':
    'adapt_growth_biogas',
    'adapt growth phs':
    'adapt_growth_phs',
    'adapt growth res elec':
    'adapt_growth_res_elec',
    'adapt co2 emissions unconv gas':
    'adapt_co2_emissions_unconv_gas',
    'adapt emissions shale oil':
    'adapt_emissions_shale_oil',
    'adapt growth biofuels 2gen':
    'adapt_growth_biofuels_2gen',
    'annual gdppc growth rate':
    'annual_gdppc_growth_rate',
    'variation pop ssp4':
    'variation_pop_ssp4',
    'variation pop ssp5':
    'variation_pop_ssp5',
    'variation pop ssp1':
    'variation_pop_ssp1',
    'variation pop ssp2':
    'variation_pop_ssp2',
    'variation pop ssp3':
    'variation_pop_ssp3',
    'annual population growth rate':
    'annual_population_growth_rate',
    'variation pop ssps':
    'variation_pop_ssps',
    'desired variation gdppc':
    'desired_variation_gdppc',
    'pop variation':
    'pop_variation',
    'variation historic gdppc':
    'variation_historic_gdppc',
    'growth labour share':
    'growth_labour_share',
    'historic new required capacity phs':
    'historic_new_required_capacity_phs',
    'initial required capacity phs':
    'initial_required_capacity_phs',
    'fed coal for heat nc':
    'fed_coal_for_heat_nc',
    'historical variation minerals extraction rest':
    'historical_variation_minerals_extraction_rest',
    'max unconv gas growth extraction':
    'max_unconv_gas_growth_extraction',
    'new res capacity for heat nc tw':
    'new_res_capacity_for_heat_nc_tw',
    'annual variation non energy use':
    'annual_variation_non_energy_use',
    'pes solids bioe ej':
    'pes_solids_bioe_ej',
    'real fe consumption solids ej':
    'real_fe_consumption_solids_ej',
    'variation demand flow fd':
    'variation_demand_flow_fd',
    'historic variation demand':
    'historic_variation_demand',
    'fed natx gas for heat nc':
    'fed_natx_gas_for_heat_nc',
    'fed oil for heat nc':
    'fed_oil_for_heat_nc',
    'pes solids':
    'pes_solids',
    'ped gas heat nc':
    'ped_gas_heat_nc',
    'ped coal heat nc':
    'ped_coal_heat_nc',
    'ped liquids heat nc':
    'ped_liquids_heat_nc',
    'ped coal ej':
    'ped_coal_ej',
    'fes heat from coal':
    'fes_heat_from_coal',
    'fes heat from natx gas':
    'fes_heat_from_natx_gas',
    'fes heat from oil':
    'fes_heat_from_oil',
    'new res capacity for heat com tw':
    'new_res_capacity_for_heat_com_tw',
    'variation historic demand':
    'variation_historic_demand',
    'variation gfcf':
    'variation_gfcf',
    'variation historic gfcf':
    'variation_historic_gfcf',
    'share consum goverment and inventories':
    'share_consum_goverment_and_inventories',
    'share consum goverments and inventories next step':
    'share_consum_goverments_and_inventories_next_step',
    'cc sectoral':
    'cc_sectoral',
    'variation cc sectoral':
    'variation_cc_sectoral',
    'fed heat com by nre chp plants ej':
    'fed_heat_com_by_nre_chp_plants_ej',
    'pe supply res non elec ej':
    'pe_supply_res_non_elec_ej',
    'new pes biogas':
    'new_pes_biogas',
    'new waste supply ej':
    'new_waste_supply_ej',
    'historic new required capacity res elec':
    'historic_new_required_capacity_res_elec',
    'share unconv gas vs tot agg':
    'share_unconv_gas_vs_tot_agg',
    'max extraction tot agg gas ej':
    'max_extraction_tot_agg_gas_ej',
    'share unconv oil vs tot agg':
    'share_unconv_oil_vs_tot_agg',
    'max extraction tot agg oil ej':
    'max_extraction_tot_agg_oil_ej',
    'extraction unconv gas ej':
    'extraction_unconv_gas_ej',
    'max extraction conv oil ej':
    'max_extraction_conv_oil_ej',
    'share chp plants oil':
    'share_chp_plants_oil',
    'share chp plants coal':
    'share_chp_plants_coal',
    'pes peat ej':
    'pes_peat_ej',
    'total gen losses demand for heat plants ej':
    'total_gen_losses_demand_for_heat_plants_ej',
    'total gen losses demand for chp plants ej':
    'total_gen_losses_demand_for_chp_plants_ej',
    'potential fe gen elec liquids chp plants ej':
    'potential_fe_gen_elec_liquids_chp_plants_ej',
    'potential fe gen elec coal chp plants ej':
    'potential_fe_gen_elec_coal_chp_plants_ej',
    'potential fe gen elec gas chp plants ej':
    'potential_fe_gen_elec_gas_chp_plants_ej',
    'fed heat gas chp plants ej':
    'fed_heat_gas_chp_plants_ej',
    'ped oil for chp plants ej':
    'ped_oil_for_chp_plants_ej',
    'ped gas for chp plants ej':
    'ped_gas_for_chp_plants_ej',
    'ped coal for chp plants ej':
    'ped_coal_for_chp_plants_ej',
    'invest nuclear tdolar':
    'invest_nuclear_tdolar',
    'nuclear capacity under construction':
    'nuclear_capacity_under_construction',
    'invest res elec tdolar':
    'invest_res_elec_tdolar',
    'initial required capacity res elec':
    'initial_required_capacity_res_elec',
    'afforestation program 2020 gtco2':
    'afforestation_program_2020_gtco2',
    'max extraction uranium ej':
    'max_extraction_uranium_ej',
    'gtco2 historic emissions rcps':
    'gtco2_historic_emissions_rcps',
    'variation historic pop':
    'variation_historic_pop',
    'tpes de castro phd scen xmadcoalx ej':
    'tpes_de_castro_phd_scen_xmadcoalx_ej',
    'tpes de castro phd scen ii ej':
    'tpes_de_castro_phd_scen_ii_ej',
    'balancing costs':
    'balancing_costs',
    'variation ctl':
    'variation_ctl',
    'variation gtl':
    'variation_gtl',
    'improvement efficiency gas for electricity':
    'improvement_efficiency_gas_for_electricity',
    'annual additional historic product biofuels 2gen':
    'annual_additional_historic_product_biofuels_2gen',
    'ped oil for heat plants ej':
    'ped_oil_for_heat_plants_ej',
    'max unconv oil growth extraction':
    'max_unconv_oil_growth_extraction',
    'extraction unconv oil ej':
    'extraction_unconv_oil_ej',
    'max extraction unconv gas':
    'max_extraction_unconv_gas',
    'max extraction unconv oil':
    'max_extraction_unconv_oil',
    'max extraction coal ej':
    'max_extraction_coal_ej',
    'max extraction conv gas ej':
    'max_extraction_conv_gas_ej',
    'ped gases for heat plants ej':
    'ped_gases_for_heat_plants_ej',
    'ped coal for heat plants ej':
    'ped_coal_for_heat_plants_ej'
}