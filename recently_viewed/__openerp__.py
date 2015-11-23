{
    'name': 'Recently Viewed Product List',
    'category': 'Website',
    'summary': 'View Your Recently Viewed Product List',
    'website': 'https://www.techhighway.co.in',
    'version': '1.0',
    'description': """
TechHighway E-Commerce
======================

        """,
    	'author'	: 'TechHighway Systems Pvt. Ltd.',
    	'depends'	: ['website', 'sale', 'payment','website_sale'],
    	'data'	: [
		'views/template.xml',
    		],
    	'qweb'	: ['static/src/xml/*.xml'],

	'images': ['static/description/recently_viewed_product_img.png'],
    	'installable': True,
    	'application': True,
}
