import random
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


CHOICES = ["rock", "paper", "scissors"]




def outcome(player: str, computer: str) -> str:
if player not in CHOICES or computer not in CHOICES:
return "invalid"
if player == computer:
return "tie"
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
return "win" if beats[player] == computer else "lose"




def index(request):
context = {"choices": CHOICES, "player": None, "computer": None, "result": None}
if request.method == "POST":
player = request.POST.get("choice")
computer = random.choice(CHOICES)
result = outcome(player, computer)
context.update({"player": player, "computer": computer, "result": result})
return render(request, "game/index.html", context)




@require_http_methods(["GET"]) # GET /api/play/?choice=rock
def play_api(request):
player = request.GET.get("choice")
computer = random.choice(CHOICES)
result = outcome(player, computer)
return JsonResponse({"player": player, "computer": computer, "result": result})