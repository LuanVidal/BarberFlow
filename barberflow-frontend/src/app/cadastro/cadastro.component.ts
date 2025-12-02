import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-cadastro',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent {
  userData = { name: '', email: '', password: '' };

  constructor(private api: ApiService, private router: Router) {}

  cadastrar() {
    // LOG 1: Ver se o botão funcionou
    console.log('Botão clicado! Tentando cadastrar:', this.userData);

    if (!this.userData.email || !this.userData.password) {
      alert('Preencha todos os campos!');
      return;
    }

    this.api.register(this.userData).subscribe({
      next: (res) => {
        // LOG 2: Sucesso
        console.log('SUCESSO! Resposta do Python:', res);
        alert('Cadastro realizado! Agora faça login.');
        this.router.navigate(['/login']);
      },
      error: (err) => {
        // LOG 3: Erro
        console.error('ERRO ao cadastrar:', err);
        alert('Erro: ' + (err.error?.error || 'Falha na conexão'));
      }
    });
  }
}