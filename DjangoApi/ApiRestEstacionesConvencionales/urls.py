
from django.urls import path
from ApiRestEstacionesConvencionales import views
urlpatterns=[
      
    
      path('t1073161h/', views.T1073161HView.as_view(), name='t1073161h'),
      path('t1073161h/<int:id>',views.T1073161HView.as_view(),name='t1073161h'),

      path('t1073161hVal/', views.T1073161HValView.as_view(), name='t1073161hVal'),
      path('t1073161hVal/<int:id>',views.T1073161HValView.as_view(),name='t1073161h'),

      path('t1123161h/', views.T1123161HView.as_view(), name='t1123161h'),
      path('t1123161h/<int:id>',views.T1123161HView.as_view(),name='t1123161h'),

      path('t1123161hVal/', views.T1123161HValView.as_view(), name='t1123161hVal'),
      path('t1123161hVal/<int:id>',views.T1123161HValView.as_view(),name='t1123161hVal'),

      path('t1263011d/', views.T1263011DView.as_view(), name='t1263011d'),
      path('t1263011d/<int:id>',views.T1263011DView.as_view(),name='t1263011d'),

      path('t1263011m/', views.T1263011MView.as_view(), name='t1263011m'),
      path('t1263011m/<int:id>',views.T1263011MView.as_view(),name='t1263011m'),

      path('t1263021d/', views.T1263021DView.as_view(), name='t1073161h'),
      path('t1263021d/<int:id>',views.T1263021DView.as_view(),name='t1073161h'),

      path('t1263021m/', views.T1263021MView.as_view(), name='t1263021m'),
      path('t1263021m/<int:id>',views.T1263021MView.as_view(),name='t1263021m'),

      path('t1263041d/', views.T1263041DView.as_view(), name='t1263041d'),
      path('t1263041d/<int:id>',views.T1263041DView.as_view(),name='t1263041d'),

      path('t1263041m/', views.T1263041MView.as_view(), name='t1263041m'),
      path('t1263041m/<int:id>',views.T1263041MView.as_view(),name='t1263041m'),

      path('t12827161h/', views.T12827161DView.as_view(), name='t12827161h'),
      path('t12827161h/<int:id>',views.T12827161DView.as_view(),name='t12827161h'),

      path('t12827161h/', views.T12827161HView.as_view(), name='t12827161h'),
      path('t12827161h/<int:id>',views.T12827161HView.as_view(),name='t12827161h'),

      path('t12827161hVal/', views.T12827161HValView.as_view(), name='t12827161hVal'),
      path('t12827161hVal/<int:id>',views.T12827161HValView.as_view(),name='t12827161hVal'),

      path('t12827161m/', views.T12827161MView.as_view(), name='t12827161m'),
      path('t12827161m/<int:id>',views.T12827161MView.as_view(),name='t12827161m'),

      path('t13028161d/', views.T13028161DView.as_view(), name='t13028161d'),
      path('t13028161d/<int:id>',views.T13028161DView.as_view(),name='t13028161d'),

      path('t13028161h/', views.T13028161HView.as_view(), name='t13028161h'),
      path('t13028161h/<int:id>',views.T13028161HView.as_view(),name='t13028161h'),

      path('t13028161hVal/', views.T13028161HValView.as_view(), name='t13028161hVal'),
      path('t13028161hVal/<int:id>',views.T13028161HValView.as_view(),name='t13028161hVal'),

      path('t13028161m/', views.T13028161MView.as_view(), name='t13028161m'),
      path('t13028161m/<int:id>',views.T13028161MView.as_view(),name='t13028161m'),

      path('t141011d/', views.T141011DView.as_view(), name='t141011d'),
      path('t141011d/<int:id>',views.T141011DView.as_view(),name='t141011d'),

      path('t141011h/', views.T141011MView.as_view(), name='t141011h'),
      path('t141011h/<int:id>',views.T141011MView.as_view(),name='t141011h'),

      path('t1410161h/', views.T1410161HView.as_view(), name='t1410161h'),
      path('t1410161h/<int:id>',views.T1410161HView.as_view(),name='t1410161h'),

      path('t1410161hVal/', views.T1410161HValView.as_view(), name='t1410161hVal'),
      path('t1410161hVal/<int:id>',views.T1410161HValView.as_view(),name='t1410161hVal'),
      
      path('t1410161hVal/', views.T1410161HValView.as_view(), name='t1410161hVal'),
      path('t1410161hVal/<int:id>',views.T1410161HValView.as_view(),name='t1410161hVal'),

      path('t141021d/', views.T141021DView.as_view(), name='t141021d'),
      path('t141021d/<int:id>',views.T141021DView.as_view(),name='t141021d'),

      path('t141021m/', views.T141021MView.as_view(), name='t141021m'),
      path('t141021m/<int:id>',views.T141021MView.as_view(),name='t141021m'),

      path('t141041d/', views.T141041DView.as_view(), name='t141041d'),
      path('t141041d/<int:id>',views.T141041DView.as_view(),name='t141041d'),

      path('t1714161d/', views.T1714161DView.as_view(), name='t1714161d'),
      path('t1714161d/<int:id>',views.T1714161DView.as_view(),name='t1714161d'),

      path('t1714161h/', views.T1714161HView.as_view(), name='t1714161h'),
      path('t1714161h/<int:id>',views.T1714161HView.as_view(),name='t1714161h'),

      path('t1714161hVal/', views.T1714161HValView.as_view(), name='t1714161hVal'),
      path('t1714161hVal/<int:id>',views.T1714161HValView.as_view(),name='t1714161hVal'),

      path('t1410161hVal/', views.T171481DView.as_view(), name='t1410161hVal'),
      path('t1410161hVal/<int:id>',views.T171481DView.as_view(),name='t1410161hVal'),

      path('t171481h/', views.T171481HView.as_view(), name='t171481h'),
      path('t171481h/<int:id>',views.T171481HView.as_view(),name='t171481h'),

      path('t171481hVal/', views.T171481HValView.as_view(), name='t171481hVal'),
      path('t171481hVal/<int:id>',views.T171481HValView.as_view(),name='t171481hVal'),

      path('t171481m/', views.T171481MView.as_view(), name='t171481m'),
      path('t171481m/<int:id>',views.T171481MView.as_view(),name='t171481m'),

      path('t187161d/', views.T187161DView.as_view(), name='t187161d'),
      path('t187161d/<int:id>',views.T187161DView.as_view(),name='t187161d'),

      path('t187161h/', views.T187161HView.as_view(), name='t187161h'),
      path('t187161h/<int:id>',views.T187161HView.as_view(),name='t187161h'),

      path('t187161hVal/', views.T187161HValView.as_view(), name='t187161hVal'),
      path('t187161hVal/<int:id>',views.T187161HValView.as_view(),name='t187161hVal'),

      path('t261111h/', views.T261111DView.as_view(), name='t261111h'),
      path('t261111h/<int:id>',views.T261111DView.as_view(),name='t261111h'),

      path('t261111m/', views.T261111MView.as_view(), name='t261111m'),
      path('t261111m/<int:id>',views.T261111MView.as_view(),name='t261111m'),

      path('t272981d/', views.T272981DView.as_view(), name='t272981d'),
      path('t272981d/<int:id>',views.T272981DView.as_view(),name='t272981d'),

      path('tT272981h/', views.T272981HView.as_view(), name='tT272981h'),
      path('tT272981h/<int:id>',views.T272981HView.as_view(),name='tT272981h'),

      path('t1410161hVal/', views.T1410161HValView.as_view(), name='t1410161hVal'),
      path('t1410161hVal/<int:id>',views.T1410161HValView.as_view(),name='t1410161hVal'),

      path('t272981hVal/', views.T272981HValView.as_view(), name='t272981hVal'),
      path('t272981hVal/<int:id>',views.T272981HValView.as_view(),name='t272981hVal'),

      path('t272981m/', views.T272981MView.as_view(), name='t272981m'),
      path('t272981m/<int:id>',views.T272981MView.as_view(),name='t272981m'),

      path('t293161d/', views.T293161DView.as_view(), name='t293161d'),
      path('t293161d/<int:id>',views.T293161DView.as_view(),name='t293161d'),

      path('t293161m/', views.T293161MView.as_view(), name='t293161m'),
      path('t293161m/<int:id>',views.T293161MView.as_view(),name='t293161m'),

      path('t29321m/', views.T29321MView.as_view(), name='t29321m'),
      path('t29321m/<int:id>',views.T29321MView.as_view(),name='t29321m'),

      path('t3211d/', views.T3211DView.as_view(), name='t3211d'),
      path('t3211d/<int:id>',views.T3211DView.as_view(),name='t3211d'),

      path('t3211m/', views.T3211MView.as_view(), name='t3211m'),
      path('t3211m/<int:id>',views.T3211MView.as_view(),name='t3211m'),

      path('t323161h/', views.T323161HView.as_view(), name='t323161h'),
      path('t323161h/<int:id>',views.T323161HView.as_view(),name='t323161h'),

      path('t323161hVal/', views.T323161HValView.as_view(), name='t323161hVal'),
      path('t323161hVal/<int:id>',views.T323161HValView.as_view(),name='t323161hVal'),

      path('t32321d/', views.T32321DView.as_view(), name='t32321d'),
      path('t32321d/<int:id>',views.T32321DView.as_view(),name='t32321d'),

      path('t32321m/', views.T32321MView.as_view(), name='t32321m'),
      path('t32321m/<int:id>',views.T32321MView.as_view(),name='t32321m'),

      path('t3711161d/', views.T3711161DView.as_view(), name='t3711161d'),
      path('t3711161d/<int:id>',views.T3711161DView.as_view(),name='t3711161d'),

      path('t3711161h/', views.T3711161HView.as_view(), name='t3711161h'),
      path('t3711161h/<int:id>',views.T3711161HView.as_view(),name='t3711161h'),

      path('t3711161hVal/', views.T3711161HValView.as_view(), name='t3711161hVal'),
      path('t3711161hVal/<int:id>',views.T3711161HValView.as_view(),name='t3711161hVal'),

      path('t42161h/', views.T42161HView.as_view(), name='t42161h'),
      path('t42161h/<int:id>',views.T42161HView.as_view(),name='t42161h'),

      path('t42161hVal/', views.T42161HValView.as_view(), name='t42161hVal'),
      path('t42161hVal/<int:id>',views.T42161HValView.as_view(),name='t42161hVal'),

      path('t573161h/', views.T573161HView.as_view(), name='t573161h'),
      path('t573161h/<int:id>',views.T573161HView.as_view(),name='t573161h'),

      path('t573161hVal/', views.T573161HValView.as_view(), name='t573161hVal'),
      path('t573161hVal/<int:id>',views.T573161HValView.as_view(),name='t573161hVal'),

      path('t583161h/', views.T583161HView.as_view(), name='t583161h'),
      path('t583161h/<int:id>',views.T583161HView.as_view(),name='t583161h'),

      path('t583161hVal/', views.T583161HValView.as_view(), name='t583161hVal'),
      path('t583161hVal/<int:id>',views.T583161HValView.as_view(),name='t583161hVal'),

      path('t597161h/', views.T597161HView.as_view(), name='t597161h'),
      path('t597161h/<int:id>',views.T597161HView.as_view(),name='t597161h'),

      path('t597161hVal/', views.T597161HValView.as_view(), name='t597161hVal'),
      path('t597161hVal/<int:id>',views.T597161HValView.as_view(),name='t597161hVal'),

      path('t603161h/', views.T603161HView.as_view(), name='t603161h'),
      path('t603161h/<int:id>',views.T603161HView.as_view(),name='t603161h'),

      path('t603161hVal/', views.T603161HValView.as_view(), name='t603161hVal'),
      path('t603161hVal/<int:id>',views.T603161HValView.as_view(),name='t603161hVal'),

      path('t613161h/', views.T613161HView.as_view(), name='t613161h'),
      path('t613161h/<int:id>',views.T613161HView.as_view(),name='t613161h'),

      path('t613161hVal/', views.T613161HValView.as_view(), name='t613161hVal'),
      path('t613161hVal/<int:id>',views.T613161HValView.as_view(),name='t613161hVal'),

      path('t614161h/', views.T614161HView.as_view(), name='t614161h'),
      path('t614161h/<int:id>',views.T614161HView.as_view(),name='t614161h'),

      path('t614161hVal/', views.T614161HValView.as_view(), name='t614161hVal'),
      path('t614161hVal/<int:id>',views.T614161HValView.as_view(),name='t614161hVal'),

      path('t621161h/', views.T621161HView.as_view(), name='t621161h'),
      path('t621161h/<int:id>',views.T621161HView.as_view(),name='t621161h'),

      path('t621161hVal/', views.T621161HValView.as_view(), name='t621161hVal'),
      path('t621161hVal/<int:id>',views.T621161HValView.as_view(),name='t621161hVal'),

      path('t644161h/', views.T644161HView.as_view(), name='t644161h'),
      path('t644161h/<int:id>',views.T644161HView.as_view(),name='t644161h'),

      path('t644161hVal/', views.T644161HValView.as_view(), name='t644161hVal'),
      path('t644161hVal/<int:id>',views.T644161HValView.as_view(),name='t644161hVal'),

      path('t644161hVal/', views.T644161HValView.as_view(), name='t644161hVal'),
      path('t644161hVal/<int:id>',views.T644161HValView.as_view(),name='t644161hVal'),

      path('t7127161d/', views.T7127161DView.as_view(), name='t7127161d'),
      path('t7127161d/<int:id>',views.T7127161DView.as_view(),name='t7127161d'),

      path('t7127161h/', views.T7127161HView.as_view(), name='t7127161h'),
      path('t7127161h/<int:id>',views.T7127161HView.as_view(),name='t7127161h'),

      path('t7127161hVal/', views.T7127161HValView.as_view(), name='t7127161hVal'),
      path('t7127161hVal/<int:id>',views.T7127161HValView.as_view(),name='t7127161hVal'),

      path('t7127161h/', views.T7127161MView.as_view(), name='t7127161h'),
      path('t7127161h/<int:id>',views.T7127161MView.as_view(),name='t7127161h'),

      path('t7229161h/', views.T7229161HView.as_view(), name='t7229161h'),
      path('t7229161h/<int:id>',views.T7229161HView.as_view(),name='t7229161h'),

      path('t734161h/', views.T734161HView.as_view(), name='t734161h'),
      path('t734161h/<int:id>',views.T734161HView.as_view(),name='t734161h'),

      path('t734161hVal/', views.T734161HValView.as_view(), name='t734161hVal'),
      path('t734161hVal/<int:id>',views.T734161HValView.as_view(),name='t734161hVal'),

      path('t775161d/', views.T775161DView.as_view(), name='t775161d'),
      path('t775161d/<int:id>',views.T775161DView.as_view(),name='t775161d'),

      path('t91161d/', views.T91161DView.as_view(), name='t91161d'),
      path('t91161d/<int:id>',views.T91161DView.as_view(),name='t91161d'),

      path('t91161h/', views.T91161HView.as_view(), name='t3711161h'),
      path('t3711161h/<int:id>',views.T91161HView.as_view(),name='t3711161h'),

      path('t91161hVal/', views.T91161HValView.as_view(), name='t91161hVal'),
      path('t91161hVal/<int:id>',views.T91161HValView.as_view(),name='t91161hVal'),

      path('t91161h/', views.T91161MView.as_view(), name='t91161h'),
      path('t91161h/<int:id>',views.T91161MView.as_view(),name='t91161h'),

      
  
     


]