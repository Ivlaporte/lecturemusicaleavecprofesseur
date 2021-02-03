from cms.utils.urlutils import admin_reverse
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from polls.models import Poll


class PollToolbar(CMSToolbar):
    supported_apps = ['polls']
    def populate(self):
        if not self.is_current_app:
            return
        menu = self.toolbar.get_or_create_menu(
            'polls_cms_integration-polls', #un unique key for this menus
            'Polls',                       #the text that should appear in the menu
        )
        menu.add_sideframe_item(
            name='Pool list',                         #name of the new item list
            url=admin_reverse('polls_poll_changelist')  #the url it should open with
        )
        menu.add_modal_item(
            name='Add a new poll',
            url=admin_reverse('polls_poll_add')
        )
        buttonlist = self.toolbar.add_button_list()
        buttonlist.add_sideframe_button(
            name='Poll list',
            url=admin_reverse('polls_poll_changelist'),
        )
        buttonlist.add_normal_button(
            name='Add a new poll',
            url=admin_reverse('polls_poll_add'),
        )
# register in tne toolbar
toolbar_pool.register(PollToolbar)
#
# 6.1.2. Add buttons to the toolba