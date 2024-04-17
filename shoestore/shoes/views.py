from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.views import View
from .models import Actor, Movie
from .forms import MovieForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# Create your views here.


###################### ACTORS ##########################

class ActorListView(ListView):
    model = Actor

class ActorCreateView(CreateView):
    model = Actor
    fields = ['name']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Actor "{actor_name}" has been created'.format(
                actor_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("movies:actor_detail", args=[self.object.id])

class ActorDetailView(DetailView):
    model = Actor

class ActorUpdateView(UpdateView):
    model = Actor
    fields = ['name']
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Actor "{actor_name}" has been updated'.format(
                actor_name=self.object.name))
        return response
    
    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("movies:actor_detail", args=[self.object.id])
        # you can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        #return reverse_lazy("movies:actor_detail",
        #                    kwargs={'pk':self.object.id})


class ActorDeleteView(DeleteView):
    model = Actor
    success_url = reverse_lazy("movies:actor_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Actor "{actor_name}" has been deleted'.format(
                actor_name=self.object.name))
        return response


###################### MOVIES ##########################


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie

class MovieUpdatebisView(View):
    def post(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, pk=self.kwargs["pk"])
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save() 
            return JsonResponse({'message': 'Movie updated successfully'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
        
class MovieDetailbisView(TemplateView):
    template_name = "movies/movie_detailbis.html"
    def get(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_id'] = self.kwargs["pk"]
        return context
    
class MovieDetailJsView(View):
    def get(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, pk=self.kwargs["pk"])
        movie_js = model_to_dict(movie)
        movie_js["actors"] = []
        for actor in movie.actors.values():
            movie_js["actors"].append(actor)
            return JsonResponse({"movie": movie_js})

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Movie "{movie_name}" has been created'.format(
                movie_name=self.object.name))
        return response

    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("movies:movie_detail", args=[self.object.id])
        # you can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        #return reverse_lazy("movies:actor_detail",
        #                    kwargs={'pk':self.object.id})




class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movies:movie_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Movie "{movie_name}" has been deleted'.format(
                movie_name=self.object.name))
        return response

class MovieUpdateView(UpdateView):
   model = Movie
   form_class = MovieForm

   def form_valid(self, form):
       response = super().form_valid(form)
       messages.add_message(
           self.request,
           messages.SUCCESS,
           'Movie "{movie_name}" has been updated'.format(
               movie_name=self.object.name
           ),
       )
       return response

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       movie_dico = model_to_dict(self.object)
       movie_dico["running_time"] = movie_dico["running_time"].strftime(
           "%H:%M:%S"
       )
       movie_dico["release_date"] = movie_dico["release_date"].strftime(
           "%Y-%m-%d"
       )
       actors = movie_dico["actors"]
       movie_actor_list = []
       for actor in actors:
           movie_actor_list.append({"id": actor.id, "name": actor.name})
       movie_dico["actors"] = movie_actor_list
       actor_list = list(Actor.objects.all().values())
       context["movie_dict"] = movie_dico
       context["actor_list"] = actor_list
       print("context", context)
       return context

   # comment the following line to show the error about not having an
   # success_url
   def get_success_url(self):
       return reverse_lazy("movies:movie_detail", args=[self.object.id])
       # you can also use it this way with kwargs, just to let you know
       # but here we have only one argument, so no mistake can be done
       # return reverse_lazy("movies:actor_detail",
       #                    kwargs={'pk':self.object.id})
   

