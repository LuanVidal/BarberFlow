import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  credentials = { email: '', password: '' };
  errorMessage = '';

  constructor(private api: ApiService, private router: Router) {}

  login() {
    this.api.login(this.credentials).subscribe({
      next: (res: any) => {
        // Salva os dados
        localStorage.setItem('user_id', res.user_id);
        localStorage.setItem('user_name', res.name);
        localStorage.setItem('role', res.role);

        // AQUI ESTÁ A MÁGICA: Redirecionamento Inteligente
        if (res.role === 'barber') {
          this.router.navigate(['/agenda']); // Barbeiro vai pra Agenda
        } else {
          this.router.navigate(['/home']);   // Cliente vai pra Home
        }
      },
      error: (err) => {
        this.errorMessage = 'E-mail ou senha inválidos.';
        console.error(err);
      }
    });
  }
}