API reference
=============

This page contains the API reference of ``br-steak`` package. The API is
split into two main sections, the core and the extensions.

.. jinja:: main_toctree

    {% if build_api %}

    .. grid:: 1 1 2 2

        .. grid-item-card:: :fa:`atom` Core
            :link: api/br/steak/core
            :link-type: doc
            :padding: 2 2 2 2

            All the core functionality of PySTK, including the main objects and
            features.

        .. grid-item-card:: :fa:`puzzle-piece` Extensions
            :link: api/br/steak/extensions
            :link-type: doc
            :padding: 2 2 2 2

            High-level routines and extensions that build on top of the core.

    .. toctree::
       :hidden:

       api/br/steak/core
       api/br/steak/extensions

    {% else %}

    .. warning::

        Set ``BUILD_API`` to ``true`` in your environment to build the API
        reference.

    {% endif %}
