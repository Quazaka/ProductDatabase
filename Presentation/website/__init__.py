from flask import Flask, render_template
import website.config
app = Flask(__name__,
           instance_relative_config=True,
           template_folder='templates')
app.config.from_object(config.DevelopmentConfig)
import website.views
