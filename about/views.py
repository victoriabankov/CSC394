from django.shortcuts import render

def about(request):
    team_members = [
        {'image_url': 'Image cap',
         'name': 'Vicky Bankov',
         'bio': 'Vicky is a senior studying Computer Science.',
         'role': 'Project Manager'
        },
        {'image_url': 'Image cap',
         'name': 'Pahul Mal',
         'bio': 'Pahul is a senior studying Computer Science.',
         'role': 'Requirements Manager'
        },
        {'image_url': 'Image cap',
         'name': 'Humberto Hurtado',
         'bio': 'Humberto is a senior studying Computer Science.',
         'role': 'Design Manager'
        },
        {'image_url': 'Image cap',
         'name': 'Belal Jaber',
         'bio': 'Belal is a senior studying Computer Science.',
         'role': 'Testing Manager'
        },
        {'image_url': 'Image cap',
         'name': 'Irving Sanchez',
         'bio': 'Irving is a senior studying Cyber Security.', 
         'role': 'Presentation Manager'
        }
    ]

    return render(request, 'about.html', {'team_members': team_members})

def register(request):
    return render(request, 'register.html')