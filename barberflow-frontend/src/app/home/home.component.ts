import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../services/api.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  barbeiros: any[] = [];
  servicos: any[] = [];
  todosHorarios: string[] = [];
  horariosFiltrados: string[] = [];

  usuarioNome: string = 'Cliente';
  isBarber: boolean = false;
  isLoading: boolean = true;
  minDate: string = '';
  meuAgendamentoAtual: any = null;

  agendamento = { barber_id: '', service_id: '', data: '', hora: '' };

  // INJETAR O ChangeDetectorRef (cd)
  constructor(
    private api: ApiService, 
    private router: Router,
    private cd: ChangeDetectorRef 
  ) {}

  ngOnInit() {
    this.usuarioNome = localStorage.getItem('user_name') || 'Cliente';
    this.isBarber = localStorage.getItem('role') === 'barber';

    // --- CORREÇÃO DA DATA (Para permitir o dia de hoje) ---
    const hoje = new Date();
    // Pega o ano, mês e dia locais manuais para não sofrer com fuso horário
    const ano = hoje.getFullYear();
    const mes = String(hoje.getMonth() + 1).padStart(2, '0'); // Janeiro é 0
    const dia = String(hoje.getDate()).padStart(2, '0');
    
    this.minDate = `${ano}-${mes}-${dia}`; // Formato YYYY-MM-DD Local
    // -----------------------------------------------------

    this.gerarTodosHorarios();
    this.carregarDadosIniciais();
  }

  gerarTodosHorarios() {
    const lista = [];
    for (let hora = 8; hora < 18; hora++) {
      if (hora === 12) continue;
      lista.push(`${hora.toString().padStart(2, '0')}:00`);
      lista.push(`${hora.toString().padStart(2, '0')}:30`);
    }
    this.todosHorarios = lista;
    this.horariosFiltrados = [...this.todosHorarios];
  }

  carregarDadosIniciais() {
    this.isLoading = true;
    const userId = Number(localStorage.getItem('user_id'));

    this.api.getUserAppointments(userId).subscribe({
      next: (data: any) => {
        const lista = Array.isArray(data) ? data : [];
        this.meuAgendamentoAtual = lista.find((a: any) => a.status === 'Agendado') || null;
        
        if (this.meuAgendamentoAtual) {
          this.finalizarCarregamento(); // Já tem agendamento
        } else {
          this.carregarListas(); // Precisa carregar formulário
        }
      },
      error: (err) => {
        console.error(err);
        this.carregarListas(); // Tenta carregar listas mesmo com erro no histórico
      }
    });
  }

  carregarListas() {
    // 1. Barbeiros
    this.api.getBarbeiros().subscribe({
      next: (data) => {
        this.barbeiros = data;
        if (this.barbeiros.length > 0 && !this.agendamento.barber_id) {
          this.agendamento.barber_id = this.barbeiros[0].id;
        }
      }, 
      error: () => this.finalizarCarregamento()
    });

    // 2. Serviços (Quando este termina, destrava a tela)
    this.api.getServices().subscribe({
      next: (data) => {
        this.servicos = data;
        this.finalizarCarregamento();
      },
      error: () => this.finalizarCarregamento()
    });
  }

  // Função auxiliar para garantir que o spinner suma
  finalizarCarregamento() {
    this.isLoading = false;
    this.cd.detectChanges(); // <--- FORÇA O ANGULAR A ATUALIZAR A TELA
  }

  atualizarHorariosDisponiveis() {
    if (!this.agendamento.barber_id || !this.agendamento.data) return;
    
    this.api.getTakenSlots(Number(this.agendamento.barber_id), this.agendamento.data)
      .subscribe((ocupados: string[]) => {
        this.horariosFiltrados = this.todosHorarios.filter(h => !ocupados.includes(h));
        this.cd.detectChanges(); // Atualiza a lista visualmente
      });
  }

  confirmarAgendamento() {
    // (Mantenha a lógica de validação anterior...)
    if (!this.agendamento.barber_id || !this.agendamento.service_id || !this.agendamento.data || !this.agendamento.hora) {
      Swal.fire('Atenção', 'Preencha todos os campos!', 'warning');
      return;
    }

    const payload = {
      user_id: localStorage.getItem('user_id'),
      barber_id: this.agendamento.barber_id,
      service_id: this.agendamento.service_id,
      date_time: `${this.agendamento.data}T${this.agendamento.hora}:00`
    };

    this.isLoading = true;
    this.api.createAppointment(payload).subscribe({
      next: () => {
        Swal.fire('Sucesso', 'Agendado!', 'success');
        this.carregarDadosIniciais();
      },
      error: (err) => {
        this.finalizarCarregamento();
        if (err.status === 409) {
          Swal.fire('Ops!', 'Horário ocupado.', 'warning');
          this.atualizarHorariosDisponiveis();
        } else {
          Swal.fire('Erro', 'Falha ao agendar.', 'error');
        }
      }
    });
  }

  logout() {
    // Limpa todos os dados salvos (ID, Nome, Role)
    localStorage.clear();
    // Redireciona para o login
    this.router.navigate(['/login']);
  }
  cancelarAgendamento() {
    if (!this.meuAgendamentoAtual) return;
    
    Swal.fire({
      title: 'Cancelar?',
      text: 'Tem certeza?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      confirmButtonText: 'Sim'
    }).then((result) => {
      if (result.isConfirmed) {
        this.isLoading = true;
        this.api.cancelAppointment(this.meuAgendamentoAtual.id).subscribe({
          next: () => {
            this.meuAgendamentoAtual = null;
            Swal.fire('Cancelado!', 'Pode agendar de novo.', 'success');
            this.carregarListas();
          },
          error: () => {
            Swal.fire('Erro', 'Não foi possível cancelar.', 'error');
            this.finalizarCarregamento();
          }
        });
      }
    });
  }
  
  irParaAgendaBarbeiro() { this.router.navigate(['/agenda']); }
}