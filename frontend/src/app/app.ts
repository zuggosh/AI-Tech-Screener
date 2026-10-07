import { Component, signal, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html'
})
export class App {
  private http = inject(HttpClient);

  resumeText = signal('');
  jobDescription = signal('');

  isLoading = signal(false);

  score = signal<number | null>(null);
  missingSkills = signal<string[]>([]);
  finalResponse = signal('');
  history = signal<string[]>([]);

  runAgents() {
    if (!this.resumeText() || !this.jobDescription()) {
      alert('Please fill in both fields');
      return;
    }

    this.isLoading.set(true);
    this.score.set(null);
    this.missingSkills.set([]);
    this.finalResponse.set('');
    this.history.set(['Sending data to AI recruiters...']);

    const payload = {
      resume_text: this.resumeText(),
      job_description: this.jobDescription()
    };

    this.http.post<any>('http://localhost:8000/api/screen', payload)
      .subscribe({
        next: (res) => {
          this.score.set(res.score);
          this.missingSkills.set(res.missing_skills);
          this.finalResponse.set(res.final_response);
          this.history.set(res.history);
          this.isLoading.set(false);
        },
        error: (err) => {
          console.error(err);
          this.history.set(['Server connection error']);
          this.isLoading.set(false);
        }
      });
  }
}