====
Home
====

Toltec is a community-maintained repository of free software for the `reMarkable tablet <https://remarkable.com/>`_.

.. raw:: html

   <img src="_static/images/toltec-large.svg" alt="" class="logo">

Install Toltec
==============

**Warning:** *Toltec does not yet support any OS build newer than OS 2.11.0.442. You will soft-brick your device if you install before support is released. See* `remarkable2-recovery <https://github.com/ddvk/remarkable2-recovery>`_ *for information on how to recover your device if you have done this.*

To install `Toltec <https://github.com/toltec-dev/toltec>`_, connect your reMarkable to Wi-Fi and paste the following lines in an `SSH session <https://remarkablewiki.com/tech/ssh>`_:

.. parsed-literal::

    wget \http://toltec-dev.org/bootstrap
    echo "|bootstrap-hash|  bootstrap" | sha256sum -c && bash bootstrap


What Does Toltec Do?
====================

Toltec gives you access to all the packages from the `Entware <https://entware.net/about.html>`_ and Toltec repositories.
Toltec keeps track of which apps you have installed and makes it easy to update or remove them.

.. container:: columns

    .. container::

        Use the **opkg** command to add, remove, and update packages from the command line.

    .. container::

        ::

            opkg update
            opkg upgrade
            opkg install <package>
            opkg remove <package>
            opkg info <package>

    .. container::

        Or install **nao** to manage packages using a graphical interface.

    .. container::

        .. image:: _static/images/nao.png
            :width: 100%
            :class: screenshot

    .. container::

        Use the **toltecctl** command to manage your Toltec install.

    .. container::

        ::

            toltecctl help
            toltecctl reenable
            toltecctl uninstall
            toltecctl switch-branch testing

To seamlessly switch between apps, start by installing a `launcher <https://toltec-dev.org/stable#section-launchers>`_.

.. raw:: html

    <p>
        <a class="button" href="stable">Browse Toltec packages</a>
        <a class="button" href="https://bin.entware.net/armv7sf-k3.2/Packages.html">Browse Entware packages</a>
    </p>


Frequently Asked Questions
==========================

Where can I get help?
    If you need help with Toltec or one of its packages, you can `start a discussion on GitHub <https://github.com/toltec-dev/toltec/discussions>`_ or `join the reMarkable community on Discord <https://discord.gg/ATqQGfu>`_.
    Please do not open issues to ask for help, as they're used exclusively for `package requests <https://github.com/toltec-dev/toltec/blob/testing/docs/contributing.md#requesting-a-package>`_ and `bug reports <https://github.com/toltec-dev/toltec/blob/testing/docs/contributing.md#reporting-a-bug>`_.

Is this supported by reMarkable AS?
    No, this is a community project.

Will this brick my reMarkable?
    Probably not, but `standard disclaimers apply <https://github.com/toltec-dev/toltec/blob/stable/LICENSE>`_.

Do you support reMarkable 2?
    Yes, Toltec will automatically detect whether you are using a reMarkable 1 or 2, and install the required framebuffer dependencies.

Can I add `__________` to Toltec?
    We’re always open to adding new packages to the repository.
    You’ll find information about how to add a package in our `contributing guide <https://github.com/toltec-dev/toltec/blob/stable/docs/contributing.md>`_.

I found a vulnerability in Toltec or one of its packages, where can I report it?
    To inform the Toltec maintainers about a security issue, please follow the `security instructions <https://github.com/toltec-dev/organization/blob/main/docs/security.md>`_.

Can I factory reset my reMarkable if I have toltec installed?
    No, **DO NOT** factory reset your reMarkable if you have toltec installed. First uninstall toltec with ``toltecctl uninstall``.

My reMarkable seems to have become unresponsive, how do I fix it?
   If you can't SSH in through USB (using IP ``10.11.99.1``), there are tools that can help you recover your reMarkable if it becomes unresponsive:

   * reMarkable 1: `uuuflash <https://github.com/ddvk/remarkable-uuuflash>`_
   * reMarkable 2: `remarkable2-recovery <https://github.com/ddvk/remarkable2-recovery>`_.
    
   If you can SSH in through USB, the following may work:

   .. parsed-literal::

      rm /etc/systemd/system/xochitl.service.d/toltec-wrapper.conf
      systemctl daemon-reload
      systemctl reset-failed xochitl
      systemctl restart xochitl
