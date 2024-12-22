from django.shortcuts import render
from .utils import get_next_idioms
from .models import Idiom

def idiom_game(request):
    context = {}
    try:
        # Fetch 4 idioms to display in the accordion
        recent_idioms = Idiom.objects.all()[:3]

        if request.method == "POST":
            input_idiom = request.POST.get('idiom', '').strip()
            
            # Check if the input idiom exists in the database
            idiom_exists = Idiom.objects.filter(text=input_idiom).exists()
            if not idiom_exists:
                context['error'] = f"成语 '{input_idiom}' 不存在，请输入一个有效的成语。"
            else:
                # Find the next idioms using custom logic
                next_idioms = get_next_idioms(input_idiom)
                context.update({
                    'input_idiom': input_idiom,
                    'next_idioms': next_idioms,
                })

        # Add the recent idioms to the context
        context['recent_idioms'] = recent_idioms

    except Exception as e:
        context['error'] = f"发生错误: {str(e)}"

    return render(request, 'idiom_game.html', context)
