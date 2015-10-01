# This is a simple script that will take a set of photos to show you what each White Balance setting looks like.
# 
# Licence: GPLv3 see here: http://www.gnu.org/licenses/gpl.html
# By Daniel Scott - 2015
# www.likecrashingwaves.com

import time
import picamera
import uuid
import os

# Declare whether you want to use annotations saying what white balance
# the shot used. It'll be printed on the actual image if its set to 1
# or higher, but nothing will print if its set to 0.
annotations = 0
# How many test shots of each white balance setting do you want to take?
shots = 3
# Set the width of the photo.
shotwidth = 1280
# Set the height of the photo.
shotheight = 720
# Set the save location of your images
path = '/home/pi/pypicamera/'

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'sunlight'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Sunlight'
    # camera.awb_gains = g
    filename = ('sunlight%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'auto'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Auto'
    # camera.awb_gains = g
    filename = ('auto%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'cloudy'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Cloudy'
    # camera.awb_gains = g
    filename = ('cloudy%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'shade'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Shade'
    # camera.awb_gains = g
    filename = ('shade%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))
    
with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'tungsten'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Tungsten'
    # camera.awb_gains = g
    filename = ('tungsten%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'fluorescent'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Fluorescent'
    # camera.awb_gains = g
    filename = ('fluorescent%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'incandescent'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Incandescent'
    # camera.awb_gains = g
    filename = ('incandescent%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'flash'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Flash'
    # camera.awb_gains = g
    filename = ('flash%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))

with picamera.PiCamera() as camera:
    camera.resolution = (shotwidth, shotheight)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'horizon'
    if annotations > 0:
        camera.annotate_text = 'White Balance: Horizon'
    # camera.awb_gains = g
    filename = ('horizon%02d{u}.jpg'.format(u=uuid.uuid4()))
    fullpath = os.path.join(path, filename)
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(fullpath % i for i in range(shots))
