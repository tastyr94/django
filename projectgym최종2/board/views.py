from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from board.models import Board, Comment
from board.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def main(request):
    return render(request, 'board/main.html')

def about(request):
    return render(request, 'board/about.html')

def food_list(request):
    return render(request, 'board/food_list.html')

def board_list(request):
    q = Board.objects.all()

    category = request.GET.get('category', '')
    if category:
        q = q.filter(category=category)
    return render(request, 'board/board_list.html',{
        'board_list': q,
    })

def board_new(request):
    return render(request, 'board/board_form.html', {
        'form': form,
    })

def board_detail(request, pk):
    board = get_object_or_404(Board, pk = pk)
    return render(request, 'board/board_detail.html', {
        'board' : board
    })

def food_detail(request, pk):
    board = get_object_or_404(Board, pk = pk)
    return render(request, 'board/food_detail.html', {
        'board' : board
    })    

@login_required
def comment_new(request, board_pk):
    #post = Post.objects.get(pk=post_pk)
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
            messages.success(request, '새 댓글을 저장했습니다')
            return redirect('/board/board_list/{}/'.format(comment.board.pk))
    else:
        form = CommentForm()
    return render(request, 'board/comment_form.html', {
        'form': form,
    })

@login_required
def comment_edit(request, board_pk, pk):
    #comment = Comment.objects.get(pk=pk)
    comment = get_object_or_404(Comment, pk=pk)

    if comment.user != request.user:
        #messages.warning(request, '댓글 작성자만 수정가능합니다.')
        return redirect('board:board_detail', board_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('/board/board_list/{}/'.format(comment.board.pk))
            messages.success(request, '댓글을 수정했습니다')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'board/comment_form.html', {
        'form': form,
    })

def comment_delete(request, board_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        #messages.warning(request, '댓글 작성자만 삭제가능합니다.')
        return redirect('board:board_detail', board_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('board:board_detail', board_pk)
    return render(request, 'board/comment_confirm_delete.html', {
        'comment': comment,
        })