from django.shortcuts import render, get_object_or_404, redirect
from .forms import GroupForm
from .models import Group
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'groups/index.html', {})
def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/group_detail.html', {'group': group})
def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.author = request.user
            group.save()
            group.members.add(request.user)
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'groups/group_edit.html', {'form': form})
def group_list(request):
    groups = Group.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'groups/group_list.html', {'groups': groups})
