# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import medialog.meadows


class MedialogMeadowsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.meadows)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.meadows:default')


MEDIALOG_MEADOWS_FIXTURE = MedialogMeadowsLayer()


MEDIALOG_MEADOWS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_MEADOWS_FIXTURE,),
    name='MedialogMeadowsLayer:IntegrationTesting',
)


MEDIALOG_MEADOWS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_MEADOWS_FIXTURE,),
    name='MedialogMeadowsLayer:FunctionalTesting',
)


MEDIALOG_MEADOWS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_MEADOWS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogMeadowsLayer:AcceptanceTesting',
)
