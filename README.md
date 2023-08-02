# Portfolio Project 5: E-commerce applications: Django

by _James Glennon_

## About / Design

### Business model

The site is for a gym/fitness centre.

The basic model is **business to customer** _B2C_.

The product is **membership to the centre**.
A possible consideration is different tiers of membership.
(e.g. swimming only, gym only, gym and swim)

The payment model should be **recurring subscription** , with ease of cancellation being a priority to the customer.
Cancellation should not imediately remove the remainder of a customer's membership time.
Ideally, bulk once-off payment which does not automatically renew should also be provided as a payment option.
Such a payment method could have a different price (i.e a discount for prepurchasing a long membership).

Both the customer and the business staff should be able to see how much longer a customer has on their membership.

### CSS

### Data model design

## Features

## Development

### Resolved Issues

#### DATABASE URL change

After changing from the local db.sqlite3 server to the elephantSQL, I attempted to change the DATABASE_URL recorded in the heroku config_vars but was unable.

The problem was addressed by deleting the associated Heroku Postgres resource. This deleted any database data currently saved on heroku, but allowed the heroku app be connected to the elephantSQL database instead.

### Known Bugs / Unresolved Issues

Logging into the Django backend through heroku live site using the '/admin' url and the superuser info returns a "csrf token missing" error.

On refreshing the page, the login attempt appears to have gone through, allowing backend maintainence.

### Testing

#### Validation and Lighthouse

## Deployment

## Room for Improvement / Expansion

## Credits

### Media

#### Favicon

Favicon by [Icons8](https://icons8.com)
[Dumbbell](https://icons8.com/icon/1784/dumbbell)

### Code

#### Hosting Staticfiles

followed steps from [W3 schools](https://www.w3schools.com/django/django_static_whitenoise.php) to display static files in development environment when 'DEBUG = False'.

#### Custom 404 Page

Followed steps from [Make Us Of](https://www.makeuseof.com/create-custom-404-error-page-django/).

#### Navigation

Python code from Code Institute's Boutique Ado walkthrough project was used to display/hide links for logged-in users / anonymous

Copied from [bootstrap documentation](https://getbootstrap.com/docs/5.3/components/navs-tabs/#base-nav)
