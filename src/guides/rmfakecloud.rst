===================================
Connecting to an rmfakecloud Server
===================================

Using `rmfakecloud <https://github.com/ddvk/rmfakecloud>`_, you can synchronize your notes and documents between Xochitl (the default reMarkable app) and alternative cloud servers.
Among other benefits, this **puts you back in control** of your data, allows you to **setup automated backups** on the server side, and gives you a web-based interface to browse your notes.

.. figure:: /_static/images/rmfakecloud-web-interface.png
    :width: 100%
    :class: screenshot

    rmfakecloud’s web interface

This page will guide you through the steps needed to connect your device to an rmfakecloud server using Toltec.

*Note: You can only be connected to one server at a time.*
*You will not be able to connect to the reMarkable cloud service and an rmfakecloud server simultaneously.*
*It is easy to* `switch between servers <#switching-to-a-different-server>`_, *though.*

Before Getting Started
----------------------

First, make sure you **have access to an account on any rmfakecloud instance**.
You can set up your own instance by following the `instructions from the repository <https://github.com/ddvk/rmfakecloud>`_.
Take note of the server address; in the following, we’ll use ``https://rmfakecloud.example.com`` as an example server address.

It’s also a good idea to **make a full backup of your data** before following the steps below.
Make sure you’ve synced your documents with the reMarkable cloud service, as you will get disconnected during the process.
The simplest way to make a backup is to `copy the contents <https://remarkablewiki.com/tech/file_transfer>`_ of ``/home/root/.local/share/remarkable`` (on your device) to a safe location.

Installing the Proxy
--------------------

Xochitl does not have built-in support for alternative servers, so we need to trick the app into *believing* it’s connecting to the main reMarkable servers even though it’s actually connecting to your server of choice.
Fortunately, Toltec provides a package that automates all these steps for you.
Start an `SSH session <https://remarkablewiki.com/tech/ssh>`_ to your device and type the following command at the prompt::

    opkg install rmfakecloud-proxy

Once the package is installed, select a server to connect to::

    rmfakecloudctl set-upstream https://rmfakecloud.example.com

Finally, run the command below to switch to that server.
This will disconnect you from the cloud (if you were connected), create a local self-signed certificate authority, and start a proxy that forwards any request directed to the official servers towards your selected server::

    rmfakecloudctl enable

If all goes well, you should get a message saying *“rmfakecloud-proxy is now enabled”* in your terminal.

Logging in to Your Account
--------------------------

Congratulations, your device is now talking to your rmfakecloud server of choice!
The last remaining step is to login to your account exactly as if you were connecting to your reMarkable account.

On your computer, browse to your rmfakecloud server’s web interface, login, then go to the *Code* tab to retrieve an eight-letter one-time-code.
On your device, go to *Menu > Settings > Account > Connect to reMarkable cloud > Connect*, then input that code.

Once this is done, you’re all set! Note that the initial sync may take some time as it will upload all your documents to the new server.

Switching to a Different Server
-------------------------------

Once the rmfakecloud proxy is setup on your device, you can switch to any other rmfakecloud instance by doing::

    rmfakecloud set-upstream https://other-rmfakecloud.example.com

Each server switch will disconnect you from the cloud, so you’ll need to log back in to your respective accounts.

Reverting Back to the reMarkable Servers
----------------------------------------

It’s easy to revert back to syncing with the reMarkable cloud service, just run the following command::

    rmfakecloud disable

After the uninstallation process completes, head to *Menu > Settings > Account > Connect to reMarkable cloud > Connect* again and input a login code from the official servers to log back in to your account.
